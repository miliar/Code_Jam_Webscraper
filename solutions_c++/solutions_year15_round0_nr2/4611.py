#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int res;
map<vector<int>, bool> vis;

void rec(vector<int> v, int t) {
	sort(v.begin(), v.end());
	v.push_back(t);
	if (vis[v])
		return;
	vis[v] = 1;
	v.pop_back();
	int mx = -(1 << 30);
	for (int i = 0; i < v.size(); i++)
		mx = max(mx, v[i]);
	res = min(res, t + mx);
	if (mx == 1)
		return;

	for (int i = 0; i < v.size(); i++) {
		vector<int> v2 = v;
		v2.push_back((1 << 30));
		if (v[i] == 1)
			continue;
		int x = (v2).size()-1;
		for (int j = 1; j < v[i] / 2 + 1; j++) {
			v2[i] = j;
			v2[x] = v[i] - j;
			rec(v2, t + 1);
		}
	}
}

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("out", "wt", stdout);
	int tests, cases = 1;
	scanf("%d", &tests);
	while (tests--) {
		int d;
		scanf("%d", &d);
		vector<int> p(d);
		for (int i = 0; i < d; ++i)
			scanf("%d", &p[i]);
		res = (1 << 30);
		vis.clear();
		rec(p, 0);
		printf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
