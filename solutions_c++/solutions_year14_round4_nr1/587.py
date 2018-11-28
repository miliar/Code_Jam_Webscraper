#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#define RD(x)      scanf("%d", &x)
#define REP(i, n)  for (int i=0; i<(n); i++)
#define FOR(i, n) for (int i=1; i<=(n); i++)
#define pii        pair<int, int>
#define mp         make_pair
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

using namespace std;
#define  N   60
#define  M   22222
#define  eps 1e-9
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 9999991ll
#define  LL  long long

int Main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; RD(T);
	FOR(_T, T) {
		int n, x; RD(n); RD(x);
		multiset<int> st;
		REP(i, n) {
			int val; RD(val);
			st.insert(val);
		}
		int ans = 0;
		while (st.size() > 0) {
			int now = *st.rbegin();
			auto po = st.find(now);
			st.erase(po);
			ans++;
			if (st.size() > 0) {
				now = x - now;
				auto p = st.upper_bound(now);
				if (p != st.begin()) {
					st.erase(--p);
				}
			}
		}
		printf("Case #%d: %d\n", _T, ans);
	}
	return 0;
}
int main() {
	return Main();
}
