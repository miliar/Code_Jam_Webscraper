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
#include <random>


typedef long long ll;
typedef long double ld;

using namespace std;

const int MAXN = 300;
const int MX = 100000;

random_device rd;
mt19937 rnd(rd());

int was[MAXN];
int sz[MAXN];
vector<int> eds[MAXN];
int p[MAXN];
char ch[MAXN];
string s[10];
int cc[10];
int n;

void dfs(int v) {
	was[v] = 1;
	sz[v] = 1;
	for (int u: eds[v]) {
		dfs(u);
		sz[v] += sz[u];
	}
}

string getS() {
	vector<int> vv;
	int sum = 0;
	for (int i = 0; i < n; ++i)
		if (p[i] == -1)
			vv.push_back(i), sum += sz[i];
	string ans;
	while (!vv.empty()) {
		int r = rnd() % sum;
		for (int i = 0; i < (int)vv.size(); ++i) {
			if (sz[vv[i]] > r) {
				ans += ch[vv[i]];
				for (int u: eds[vv[i]])
					vv.push_back(u);
				vv.erase(vv.begin() + i);
				--sum;
				break;
			}
			else {
				r -= sz[vv[i]];
			}
		}
	}
	return ans;
}

void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		eds[i].clear(), was[i] = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", p + i);
		--p[i];
		if (p[i] != -1)
			eds[p[i]].push_back(i);
	}
	for (int i = 0; i < n; ++i)
		if (!was[i])
			dfs(i);
	for (int i = 0; i < n; ++i)
		cin >> ch[i];
	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; ++i)
		cin >> s[i];
	for (int i = 0; i < m; ++i)
		cc[i] = 0;
	for (int i = 0; i < MX; ++i) {
		string t = getS();
		for (int j = 0; j < m; ++j) {
			if (strstr(t.c_str(), s[j].c_str()))
				++cc[j];
		}
	}
	for (int i = 0; i < m; ++i)
		printf(" %f", (double)cc[i] / MX);
	printf("\n");
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d:", i + 1);
		solve();
	}
	return 0;
}


