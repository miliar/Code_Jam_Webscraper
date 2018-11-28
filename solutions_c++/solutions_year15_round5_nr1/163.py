/*
 * Problem : 
 * Author : Hwhitetooth
 * Date : 
 * Result :
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 1000000 + 10;

vector<int> e[N];
int vis[N];
int s[N], low[N], high[N];
pair<int, int> a[N];
int testCases, n, d;

int main() {
	cin >> testCases;
	for (int _ = 1; _ <= testCases; ++_) {
		cin >> n >> d;
		for (int i = 0; i < n; ++i) {
			e[i].clear();
		}
		int as, cs, rs, m0, am, cm, rm;
		cin >> s[0] >> as >> cs >> rs;
		cin >> m0 >> am >> cm >> rm;
		for (int i = 1; i < n; ++i) {
			s[i] = (1LL * s[i - 1] * as % rs + cs) % rs;
			m0 = (1LL * m0 * am % rm + cm) % rm;
			e[m0 % i].push_back(i);
		}
		memset(vis, 0, sizeof vis);
		low[0] = high[0] = s[0];
		queue<int> que;
		que.push(0);
		vis[0] = 1;
		int x, y;
		while (!que.empty()) {
			x = que.front();
			que.pop();
			for (int i = 0; i < (int)e[x].size(); ++i) {
				y = e[x][i];
				if (! vis[y]) {
					low[y] = min(low[x], s[y]);
					high[y] = max(high[x], s[y]);
					que.push(y);
				}
			}
		}
		for (int i = 0; i < n; ++i) {
//			cerr << i << ' ' << low[i] << ' ' << high[i] << endl;
			a[i].first = high[i];
			a[i].second = low[i];
		}
		sort(a, a + n);
		int l, r = 0, ans = 1;
		priority_queue<int> heap;
		for (int h = s[0]; h <= a[n - 1].first; ++h) {
			for (; r < n && a[r].first <= h; ++r) {
				heap.push(-a[r].second);
			}
			int l = h - d;
			for (; !heap.empty() && -heap.top() < l; heap.pop());
			ans = max(ans, (int)heap.size());
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}