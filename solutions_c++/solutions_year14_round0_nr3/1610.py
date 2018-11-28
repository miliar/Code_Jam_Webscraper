#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int map[27][27];
bool vis[27][27];
int dr[8] = {-1,-1,-1,0,0,1,1,1};
int dc[8] = {-1,0,1,-1,1,-1,0,1};
int ax,ay;

int cnt(int n)
{
	int ans = 0;
	while(n) {
		n = n & (n-1);
		++ans;
	}
	return ans;
}

void fillmap(int r,int c)
{
	for(int i = 1; i <= r; ++i)
		for(int j = 1; j <= c; ++j) 
			if(map[i][j] != -2) 
				for(int k = 0; k < 8; ++k) 
					if(map[i+dr[k]][j+dc[k]] == -2)
						++map[i][j];
}

int rev(int x,int y)
{
	if(vis[x][y]) return 0;
	int cnt = 1;
	vis[x][y] = true;
	if(map[x][y] == 0) {
		for(int i = 0; i < 8; ++i) 
			if(map[x+dr[i]][y+dc[i]] >= 0) 
				cnt += rev(x+dr[i],y+dc[i]);
	}
	return cnt;
}
bool attempt(int r,int c,int m)
{
	for(int i = 1; i <= r; ++i)
		for(int j = 1; j <= c; ++j) {
			ax = i; ay = j;
			memset(vis,0,sizeof(vis));
			if(rev(i,j) == r*c-m) 
				return true;
		}
	return false;
}
bool solve(int r,int c,int m)
{
	int tot = r * c;
	for(int i = 0; i < 1 << tot; ++i) {
		if(cnt(i) == m) {
			memset(map,-1,sizeof(map));
			int t = i;
			for(int i = 1; i <= r; ++i) 
				for(int j = 1; j <= c; ++j) {
					++map[i][j];
					if(t & 1) map[i][j] = -2;
					t >>= 1;
				}
			fillmap(r,c);
			if(attempt(r,c,m)) return true;
		}
	}
	return false;
}
int main()
{
	freopen("/home/leo/in.txt","r",stdin);
	freopen("/home/leo/out.txt","w",stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int r,c,m;
		cin >> r >> c >> m;
		cout << "Case #" << t << ":" << endl;
		if(!solve(r,c,m)) {
			cout << "Impossible" << endl;
		} else {
			for(int i = 1; i <= r; ++i) {
				for(int j = 1; j <= c; ++j) {
					if(ax == i && ay == j) {
						cout << "c";
					} else if(vis[i][j]) {
						cout << ".";
					} else cout << "*";
				}
				cout << endl;
			}
		}
	}
}
