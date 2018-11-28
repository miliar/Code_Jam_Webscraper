/*************************************************************************
	> Author: Wayne Ho
	> Purpose: TODO
	> Created Time: Sat Apr 11 22:59:11 2015
	> Mail: hewr2010@gmail.com 
 ************************************************************************/
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int maxn = 1100;
int a[maxn];

int main(int argc, char **argv) {
	freopen("b-large.in", "r", stdin);
	int Cases;
	cin >> Cases;
	for (int Case = 1; Case <= Cases; ++Case) {
		int n, m(0);
		cin >> n;
		memset(&a, 0, sizeof(a));
		for (int i = 0; i < n; ++i) {
			int x;
			cin >> x;
			++a[x];
			m = max(m, x);
		}
		int ans(m);
		for (int gap = 1; gap <= m; ++gap) if (gap < ans) {
			int now(gap);
			for (int i = gap + 1; i <= m; ++i) {
				int moves = (i - 1) / gap;
				now += moves * a[i];
			}
			if (now < ans) ans = now;
		}
		cout << "Case #" << Case << ": " << ans << endl;
	}

    return 0;
}

