#include <bits/stdc++.h>

using namespace std;

#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define ABS(a) (((a) > (0)) ? (a) : (-1 * (a)))

int max2(int a[], int x, int y) {
	int max = 0;
	for (int i = x; i <= y; i++) {
		if (a[i] > 0) {
			max = i;
		}
	}

	return max;
}

int main() {
	int t;
	
	ifstream cin;
	cin.open("B-small-attempt8.in");

	ofstream cout;
	cout.open("out.txt");
	
	cin >> t;

	for (int z = 1; z <= t; z++) {
		int n;
		cin >> n;
		int a[n];

		int res = 100000;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		sort(a, a + n);

		for (int i = 1; i < 10; i++) {
			int tmp = 0;
			for (int j = 0; j < n; j++) {
				if (i > a[j]) {
					continue;
				}

				int tmp2 = a[j] - i;
				int tmp3 = tmp2 / i;
				tmp += tmp3;
				if (tmp2 % i) {
					tmp++;	
				}
			}
			//cout << tmp << endl;
			res = MIN(res, tmp + i);
		}	

		cout << "Case #" << z << ": " << res << endl;
	}
}