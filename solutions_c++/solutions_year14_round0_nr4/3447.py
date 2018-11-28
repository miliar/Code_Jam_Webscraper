#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int NMAX = 1000;
int T, n;
double a[NMAX], b[NMAX];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		for (int i = 0; i < n; i++) {
			cin >> b[i];
		}
		sort(a, a + n);
		sort(b, b + n);
		int nao = 0, ken = 0, ans1 = 0, ans2 = 0;
		while (nao < n)
		{
			while (nao < n && a[nao] < b[ken])
				nao++;
			if (nao < n) ans1++;
			nao++; ken++;
		}
		nao = 0, ken = 0;
		while (ken < n)
		{
			while (ken < n && a[nao] > b[ken])
				ken++;
			if (ken < n) ans2++;
			ken++; nao++;
		}
		printf("Case #%d: %d %d\n", t + 1, ans1, n - ans2);

	}
	return 0;
}