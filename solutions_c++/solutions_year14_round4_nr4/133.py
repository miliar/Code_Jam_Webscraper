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

const int M = 8;
const int N = 4;
const int L = 100 + 10;
const int T = 1000000;

vector<int> a[N];
char s[M][L];
int n, m;
int testCases;
int trie[T][26];
int totNodes;
int ans, cnt;

int newNode()
{
	int t = totNodes++;
	for (int i = 0; i < 26; ++i) trie[t][i] = -1;
	return t;
}

void insert(int t, int x)
{
	int len = strlen(s[x]);
	for (int i = 0; i < len; ++i) {
		int j = s[x][i] - 'A';
		if (trie[t][j] == -1) trie[t][j] = newNode();
		t = trie[t][j];
	}
}

void update()
{
	for (int i = 0; i < n; ++i)
		if (! a[i].size()) return;
	totNodes = 0;
	for (int i = 0; i < n; ++i) {
		int t = newNode();
		for (int j = 0; j < a[i].size(); ++j) insert(t, a[i][j]);
	}
/*	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < a[i].size(); ++j) cerr << a[i][j] << ' ';
		cerr << endl;
	}
//	cerr << "ans : " << totNodes + 1 << endl;
*/	
	if (totNodes > ans) {
		ans = totNodes;
		cnt = 1;
	}
	else
		if (totNodes == ans) ++cnt;
}

void dfs(int x)
{
	if (x == m) {
		update();
		return;
	}
	for (int i = 0; i < n; ++i) {
		a[i].push_back(x);
		dfs(x + 1);
		a[i].pop_back();
	}
}

int main()
{
	cin >> testCases;
	for (int t = 1; t <= testCases; ++t) {
		ans = 0;
		
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i) scanf("%s", s[i]);
		dfs(0);
		
		printf("Case #%d: %d %d\n", t, ans, cnt);
	}
	return 0;
}
