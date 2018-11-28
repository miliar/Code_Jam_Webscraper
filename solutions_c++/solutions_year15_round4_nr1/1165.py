#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))

int t, n, m;
char g[100][101];
vector<int>r[100], c[100];
int dr[] = { 0, 0, 1, -1 };
int dc[] = { 1, -1, 0, 0 };
bool DFS(int r, int c ,int k){
	if (r < 0 || c < 0 || r == n || c == m)
		return 1;
	if (g[r][c] != '.')
		return 0;
	return DFS(r + dr[k], c + dc[k],k);
}
bool check(int x, int y) {
	int s = 0;
	for (int i = 0; i < 4; ++i){
		int nr = dr[i] + x;
		int nc = dc[i] + y;
		s += DFS(nr, nc, i);
	}
	return s == 4;
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n >> m;
		FOR(0, n)
			r[i].clear();
		FOR(0, m)
			c[i].clear();
		FOR(0, n){
			scanf("%s", g[i]);
			for (int j = 0; j < m; ++j){
				if (g[i][j] == '.')
					continue;
				r[i].push_back(j);
				c[j].push_back(i);
			}
		}
		bool imp = 0;
		int res = 0;
		FOR(0, n){
			if (r[i].size()){
				if (g[i][r[i][0]] == '<'){
					if (check(i, r[i][0]))
						imp = 1;
					++res;
				}
				if (g[i][r[i].back()] == '>'){
					if (check(i, r[i].back()))
						imp = 1;
					++res;
				}
			}
		}
		FOR(0, m){
			if (c[i].size()){
				if (g[c[i][0]][i] == '^'){
					if (check(c[i][0], i))
						imp = 1;
					++res;
				}
				if (g[c[i].back()][i] == 'v'){
					if (check(c[i].back(), i))
						imp = 1;
					++res;
				}
			}
		}
		if (imp){
			printf("Case #%d: IMPOSSIBLE\n", k);
			continue;
		}
		printf("Case #%d: %d\n", k, res);
	}
}