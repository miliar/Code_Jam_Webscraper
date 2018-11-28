#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

const int N = 100000 + 10;

int n, m;
int tot;
int maxv, cnt;
int val[N];
vector<string> vec[N];
string s[N];
int ch[N][26];

void ins(string s)
{
	int cur = 0;
	for(int i = 0; i < s.size(); ++ i) {
		int c = s[i] - 'A';
		if (ch[cur][c] == 0) {
			ch[cur][c] = tot;
			memset(ch[tot], 0, sizeof ch[tot]);
			tot ++;
		}
		cur = ch[cur][c];
	}
}

int check(vector<string> vec)
{
	if (vec.empty()) return 0;
	tot = 1;
	memset(ch[0], 0, sizeof ch[0]);
	foreach(it, vec) {
		ins(*it);
	}
	return tot;
}

void check()
{
	for(int i = 0; i < n; ++ i) {
		vec[i].clear();
	}
	for(int i = 0; i < m; ++ i) {
		vec[val[i]].push_back(s[i]);
	}
	int ret = 0;
	for(int i = 0; i < n; ++ i) {
		ret += check(vec[i]);
	}
	if (ret > maxv) {
		maxv = ret;
		cnt = 1;
	} else if (ret == maxv) {
		++ cnt;
	}
}

void dfs(int u)
{
	if (u == m) {
		check();
		return;
	}
	for(int i = 0; i < n; ++ i) {
		val[u] = i;
		dfs(u + 1);
	}
}

void solve(int test)
{
	cerr << test << endl;
	printf("Case #%d: ", test);
	cin >> m >> n;
	for(int i = 0; i < m; ++ i) {
		cin >> s[i];
	}
	cnt = 0;
	maxv = -1;
	dfs(0);
	cout << maxv << ' ' << cnt << endl;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin); freopen("D-small-attempt0.out", "w", stdout);
	//freopen("D-small-attempt1.in", "r", stdin); freopen("D-small-attempt1.out", "w", stdout);
	//freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
