#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 25;

int n;

char map[N][N + 1];

int fa[N * 2];

int find(int u) {
	return fa[u] == u ? u : fa[u] = find(fa[u]);
}

const int INF = 1000000000;

int solve(vector<pair<int, int> > ps) {
	if (ps.size() == 1) {
		return ps.back().first * ps.back().second;
	} else {
		int ret = INF;
		vector<pair<int, int> > tmp;
		if (ps.back().first == ps.back().second) {
			tmp = ps;
			tmp.pop_back();
			ret = min(ret, solve(tmp) + ps.back().first * ps.back().second);
		}
		for (int i = (int)ps.size() - 2; i >= 0; --i) {
			if (i != ps.size() - 2 && ps[i] == ps[i + 1]) {
				continue;
			}
			tmp = ps;
			tmp.back().first += tmp[i].first;
			tmp.back().second += tmp[i].second;
			tmp.erase(tmp.begin() + i);
			ret = min(ret, solve(tmp));
		}
		return ret;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		scanf("%d", &n);
		for (int i = 0; i < n + n; ++i) {
			fa[i] = i;
		}
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%s", map[i]);
			for (int j = 0; j < n; ++j) {
				if (map[i][j] == '1') {
					++cnt;
					fa[find(i)] = find(n + j);
				}
			}
		}
		vector<pair<int, int> > ps;
		for (int i = 0; i < n * 2; ++i) {
			if (find(i) == i) {
				pair<int, int> b = make_pair(0, 0);
				for (int j = 0; j < n * 2; ++j) {
					if (find(j) == i) {
						if (j < n) {
							++b.first;
						} else {
							++b.second;
						}
					}
				}
				ps.push_back(b);
			}
		}
		sort(ps.begin(), ps.end());
		reverse(ps.begin(), ps.end());
		printf("%d\n", solve(ps) - cnt);
	}
	return 0;
}
