#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#define MX 1001
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t;
	cin >> t;

	for (int tsc = 1; tsc <= t; tsc++){
		int n, x, ans1 = 0, ans2 = 0;
		cin >> n;

		vector<double> a(n + 1, 0), b(n + 1, 0), c(n + 1, 0);

		for (int i = 0; i < n; i++)
			cin >> a[i];

		for (int i = 0; i < n; i++)
			cin >> b[i];

		sort(a.begin(), a.begin() + n);
		sort(b.begin(), b.begin() + n);

		for (int i = 0; i < n; i++) {
			c[i] = b[i];
		}

		int i, j;
		for (i = n - 1; i >= 0; i--) {
			bool fnd = false;
			int idx = -1;

			for (j = n - 1; j >= 0; j--) {
				if (c[j] != -1 && c[j] > a[i]) {
					fnd = true;
					idx = j;
				}
				else if (c[j] != -1) {
					break;
				}
			}

			ans2++;
			if (fnd) {
				c[idx] = -1;
				ans2--;
			}
			else {
				j = 0;
				while (j < n && c[j] != -1)
					j++;
				c[j] = -1;
			}
		}

		i = 0, j = 0;
		while (i < n && j < n) {
			if (a[i] > b[j])
				i++, ans1++, j++;
			else i++;
		}

		printf("Case #%d: %d %d\n", tsc, ans1, ans2);
	}
	return 0;
}
