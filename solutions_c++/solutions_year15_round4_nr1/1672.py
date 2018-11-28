#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <tr1/unordered_map>
#include <windows.h>

using namespace std;
using namespace tr1;

#define ft first
#define sd second

typedef long long LL;
typedef unsigned int UI;

const int MAXN = 511111;
const int MOD = 1e9 + 7;
const double eps = 1e-6;
const LL MAXL = (LL)(0x7fffffffffffffff);
const int MAXI = 0x7fffffff;


string mat[111];
int vis[111][111];
bool yes[111111];
pair<int, int> id[111][111];

void trans(int &x, int &y, char a){
	if(a == '^') x--;
	else if(a == '<') y--;
	else if(a == '>') y++;
	else x++;
}


int n, r, c;

int d[4][2] = { 0, 1, 1, 0, 0, -1, -1, 0 };

map<pair<int, int>, int> mp;

pair<int, int> dfs(int x, int y, char dir){
	if(vis[x][y] && mat[x][y] != '.'){
		id[x][y] = make_pair(x, y);
		return id[x][y];
	}
	vis[x][y] = true;
	if((id[x][y].ft != -1 || id[x][y].sd != -1) && mat[x][y] != '.'){
		return id[x][y];
	}
	if(mat[x][y] != '.') dir = mat[x][y];
	int nx = x, ny = y;
	trans(nx, ny, dir);
	if(nx < 0 || ny < 0 || nx >= r || ny >= c){
		id[x][y] = make_pair(x, y);
		yes[id[x][y].ft * c + id[x][y].sd] = false;
	}
	else{
		id[x][y] = dfs(nx, ny, dir);
	}
	return id[x][y];
}

char x[6] = "<>^v";


int main(){

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	

	int T;
	cin >> T;
	for(int cases = 1; cases <= T; cases++){
		mp.clear();
		memset(vis, 0, sizeof(vis));
		memset(yes, 1, sizeof(yes));
		cin >> r >> c;
		for(int i = 0; i < r; i++){
			cin >> mat[i];
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				id[i][j] = make_pair(-1, -1);
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] != '.' && (id[i][j].ft == -1 || id[i][j].sd != -1)){
					dfs(i, j, mat[i][j]);
					memset(vis, 0, sizeof(vis));
				}
			}
		}
		for(int i = 0 ; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] != '.') mp[id[i][j]]++;
			}
		}
		bool yy = true;
		int ans = 0;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] == '.') continue;
				//cout << i << " "<< j << " " << id[i][j].ft << " " << id[i][j].sd << endl;
				if(id[i][j].ft != -1 && id[i][j].sd != -1 && mp[id[i][j]] < 2){
					bool y = false;
					for(int k = 0; k < 4 && !y; k++){
						for(int w = 0, nx = i, ny = j; w < 111; w++, nx += d[k][0], ny += d[k][1]){
							if(nx < 0 || ny < 0 || nx >= r || ny >= c) break;
							if((nx != i || ny != j) && mat[nx][ny] != '.'){
								y = true;
								break;
							}
						}
					}
					if(y) ans++;
					else yy = false;
				}
				else{
					if(!yes[id[i][j].ft * c + id[i][j].sd]){
						ans++;
						yes[id[i][j].ft * c + id[i][j].sd] = true;
					}
				}
			}
		}
		printf("Case #%d: ", cases);
		if(yy) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}
