#include <bits/stdc++.h>

using namespace std;

struct sen {
	int no;
	char name;
};

bool fn(sen a, sen b)
{
	return a.no > b.no;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small-out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int k = 0; k < t; k++) {
		int n;
		cin >> n;

		sen a[n];

		int sum = 0;

		for (int i = 0; i < n; i++) {
			cin >> a[i].no;
			a[i].name = char('A' + i);

			sum += a[i].no;
		}
		cout << "Case #" << k + 1 << ": ";

		while (sum) {
			sort(a, a + n, fn);
			sum--;
			a[0].no--;
			cout << a[0].name;

			sort(a, a + n, fn);
			if (a[0].no > sum / 2) {
				sum--;
				a[0].no--;
				cout << a[0].name;
			}
			cout << ' ';
		}
		cout << endl;
	}

	return 0;
}
