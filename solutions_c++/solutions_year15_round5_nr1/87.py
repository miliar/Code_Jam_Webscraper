#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

const int MAXN = 1000010;

int cnt;

int n, d;

vector<int> go[1000010];
vector<int> eds[MAXN];
int en[MAXN];
ll s[MAXN];
ll m[MAXN];
ll as, cs, rs;
ll am, cm, rm;

void dfs(int v) {
	assert(en[v] == 1);
	--cnt;
	en[v] = 0;
	for (int i = 0; i < (int)eds[v].size(); ++i) {
		int u = eds[v][i];
		if (en[u])
			dfs(u);
	}
}

void dfs2(int v, int l) {
	assert(en[v] == 0);
	++cnt;
	en[v] = 1;
	for (int i = 0; i < (int)eds[v].size(); ++i) {
		int u = eds[v][i];
		if (s[u] >= l && s[u] <= l + d)
			dfs2(u, l);
	}
}


int solve() {
	scanf("%d%d", &n, &d);
	scanf("%lld%lld%lld%lld", &s[0], &as, &cs, &rs);
	scanf("%lld%lld%lld%lld", &m[0], &am, &cm, &rm);
	for (int i = 1; i < n; ++i)
		s[i] = (s[i - 1] * as + cs) % rs;
	for (int i = 1; i < n; ++i)
		m[i] = (m[i - 1] * am + cm) % rm;
	m[0] = 0;
	for (int i = 0; i < n; ++i)
		eds[i].clear(), en[i] = 0;
	for (int i = 1; i < n; ++i) {
		m[i] = m[i] % i;
		eds[m[i]].push_back(i);
	}
	

	for (int i = 0; i <= 1000004; ++i)
		go[i].clear();
	for (int i = 0; i < n; ++i) {
		go[s[i]].push_back(i);
	}
	int ans = 0;
	cnt = 0;
	for (int i = -d - 1; i + d + 1 <= 1000004; ++i) {
		if (i >= 0) {
			for (auto j: go[i]) {
				if (!en[j])
					continue;
				dfs(j);
			}
		}
		for (auto j: go[i + d + 1]) {
			if (j == 0 || en[m[j]]) {
				if (!en[j])
					dfs2(j, i + 1);
			}
		}
		ans = max(ans, cnt);
	}
	return ans;
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}


