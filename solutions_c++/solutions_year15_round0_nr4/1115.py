#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
int n, m, x;
bool vis[5][5];
int dx3[2][3] = { { 0, 0, 0 }, { 0, 0, 1 } };
int dy3[2][3] = { { 0, 1, 2 }, { 0, 1, 1 } };
int dx4[5][4] = { { 0, 0, 0, 0 }, { 0, 0, 1, 1 }, { 0, 0, 1, 2 }, { 0, -1, 0, 1 }, { 0, 1, 1, 2 } };
int dy4[5][4] = { { 0, 1, 2, 3 }, { 0, 1, 0, 1 }, { 0, 1, 1, 1 }, { 0, 1, 1, 1 }, { 0, 0, 1, 1 } };
vector < vector<pair<int, int> > >v[2];
vector < vector<pair<int, int> > >g[5];
bool solve1(int S, int sum){
	if (sum == n * m)
		return true;
	bool ret = false;
	for (int type = 0; type < 2; ++type){
		if (sum == 0 && type != S)
			continue;
		for (int r = 0; r < n; ++r){
			for (int c = 0; c < m; ++c){
				if (vis[r][c])
					continue;
				for (int k = 0; k < v[type].size(); ++k){
					bool can = 1;
					vector<pair<int, int> > s = v[type][k];
					for (int l = 0; l < s.size(); ++l){
						int nr = s[l].first + r;
						int nc = s[l].second + c;
						if (nr < 0 || nc < 0 || nr >= n || nc >= m || vis[nr][nc]){
							can = 0;
							break;
						}
					}
					if (!can)
						continue;
					for (int l = 0; l < s.size(); ++l)
						vis[s[l].first + r][s[l].second + c] = 1;
					ret |= solve1(S, sum + 3);
					for (int l = 0; l < s.size(); ++l)
						vis[s[l].first + r][s[l].second + c] = 0;
				}
			}
		}
	}
	return ret;
}
bool solve2(int S, int sum){
	if (sum == n * m)
		return true;
	bool ret = false;
	for (int type = 0; type < 5; ++type){
		if (sum == 0 && type != S)
			continue;
		for (int r = 0; r < n; ++r){
			for (int c = 0; c < m; ++c){
				if (vis[r][c])
					continue;
				for (int k = 0; k < g[type].size(); ++k){
					bool can = 1;
					vector<pair<int, int> > s = g[type][k];
					for (int l = 0; l < s.size(); ++l){
						int nr = s[l].first + r;
						int nc = s[l].second + c;
						if (nr < 0 || nc < 0 || nr >= n || nc >= m || vis[nr][nc]){
							can = 0;
							break;
						}
					}
					if (!can)
						continue;
					for (int l = 0; l < s.size(); ++l)
						vis[s[l].first + r][s[l].second + c] = 1;
					ret |= solve2(S, sum + 4);
					for (int l = 0; l < s.size(); ++l)
						vis[s[l].first + r][s[l].second + c] = 0;
				}
			}
		}
	}
	return ret;
}																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				
vector<pair<int, int> > reflect(vector<pair<int, int> > a, bool xd, bool yd){
	for (int i = 0; i < a.size(); ++i){
		if (xd)
			a[i].first *= -1;
		if (yd)
			a[i].second *= -1;
	}
	return a;
}
vector<pair<int, int> > rotate(vector<pair<int, int> > a){
	for (int i = 0; i < a.size(); ++i)
		swap(a[i].first, a[i].second);
	return a;
}
int main(){
	for (int i = 0; i < 2; ++i){
		vector<pair<int, int> >a;
		for (int j = 0; j < 3; ++j)
			a.push_back(make_pair(dx3[i][j], dy3[i][j]));
		v[i].push_back(a);
		if (i){
			v[i].push_back(reflect(a, 1, 0));
			v[i].push_back(reflect(a, 1, 1));
			v[i].push_back(reflect(a, 0, 1));
		}
		else{
			v[i].push_back(reflect(a, 1, 1));
			v[i].push_back(rotate(a));
			v[i].push_back(reflect(rotate(a), 1, 1));
		}
	}
	for (int i = 0; i < 5; ++i){
		vector<pair<int, int> >a;
		for (int j = 0; j < 4; ++j)
			a.push_back(make_pair(dx4[i][j], dy4[i][j]));
		g[i].push_back(a);
		if (i == 0 || i == 3){
			g[i].push_back(reflect(a, 1, 1));
			g[i].push_back(rotate(a));
			g[i].push_back(reflect(rotate(a), 1, 1));
		}
		if (i == 1 || i == 2){
			g[i].push_back(reflect(a, 1, 0));
			g[i].push_back(reflect(a, 1, 1));
			g[i].push_back(reflect(a, 0, 1));
		}
		if (i == 2){
			g[i].push_back(rotate(a));
			g[i].push_back(reflect(rotate(a), 1, 0));
			g[i].push_back(reflect(rotate(a), 1, 1));
			g[i].push_back(reflect(rotate(a), 0, 1));
		}
		if (i == 4){
			g[i].push_back(rotate(a));
			g[i].push_back(reflect(a, 0, 1));
			g[i].push_back(reflect(rotate(a), 0, 1));
		}
	}
	int t;
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> x >> n >> m;
		bool yes = 0;
		if (x == 1)
			yes = 1;
		if (x == 2 && (n % 2 == 0 || m % 2 == 0))
			yes = 1;
		if (x == 3){
			yes = 1;
			for (int i = 0; i < 2; ++i){
				memset(vis, 0, sizeof(vis));
				yes &= solve1(i, 0);
			}
		}
		if (x == 4){
			yes = 1;
			for (int i = 0; i < 5; ++i){
				memset(vis, 0, sizeof(vis));
				bool w = solve2(i, 0);
				yes &= w;
			}
		}
		if (yes)
			printf("Case #%d: GABRIEL\n",k);
		else
			printf("Case #%d: RICHARD\n", k);
	}
}