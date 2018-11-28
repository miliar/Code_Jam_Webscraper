#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <iomanip>
#include <sstream>

#define abs(x) ((x)>0?(x):-(x))
#define sqr(x) ((x)*(x))

#define all(x) x.begin(), x.end()
#define rall(v) v.rbegin(),v.rend()

#define ll long long
#define ull unsigned long long

#define FOR(i,a,b)		for(int i=(a); i<(b);i++)
#define FF(i,a)			for(int i=0; i<(a);i++)
#define FFD(i,a)		for(int i=(a)-1; i>=0;i--)
#define CC(m,what)		memset(m,what,sizeof(m))
#define SZ(a)			((int)a.size())
#define viewPP(a,n,m)	{puts("---");FF(i,n){FF(j,m) cout<<a[i][j] <<' ';puts("");}}
#define viewP(a, n)     {FF(i, n) {cout<<a[i]<<" ";} puts("");}

#define read			freopen("in.txt","r",stdin)
#define write			freopen("out.txt","w",stdout)

const double eps = 1e-11;
const int inf = 0x7fffffff;
const int hinf = 0x3f3f3f3f;
const double pi = 3.1415926535897932;

int dx[] = {-1, 0, 1, 0,  -1, 1,  1, -1};//up Right down Left
int dy[] = {0,  1, 0, -1,  1, 1, -1, -1};

using namespace std;
char Map[5][5];
bool judge(int x, int y) {
	if(x >= 0 && x < 4 && y >= 0 && y < 4) 
		return true;
	return false;
}

int solve() {
	int f = 0;
	FF(i, 4) {
		FF(j, 4) {
			if(Map[i][j] == '.')
				f = 1;
			if(Map[i][j] == 'X' || Map[i][j] == 'O') {
				FF(k, 8) {
					int nx = i+dx[k];
					int ny = j+dy[k];
					int ct = 0;
					while(judge(nx, ny) && Map[nx][ny] == Map[i][j]) {
						nx += dx[k];
						ny += dy[k];
						ct++;
					}
					if(ct >= 3) {
						if(Map[i][j] == 'X')
							return 1;
						if(Map[i][j] == 'O')
							return -1;
					}
				}
			}
			if(Map[i][j] == 'T') {
				FF(k, 8) {
					int nx = i+dx[k];
					int ny = j+dy[k];
					int ct = 0;
					while(judge(nx, ny) && Map[nx][ny] == 'X') {
						nx += dx[k];
						ny += dy[k];
						ct++;
					}
					if(ct >= 3) {
						return 1;
					}
				}
				FF(k, 8) {
					int nx = i+dx[k];
					int ny = j+dy[k];
					int ct = 0;
					while(judge(nx, ny) && Map[nx][ny] == 'O') {
						nx += dx[k];
						ny += dy[k];
						ct++;
					}
					if(ct >= 3) {
						return -1;
					}
				}
			}
		}
	}
	if(f)
		return -2;
	else
		return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
	//A-small-attempt0
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
	int cas, cas_c = 1;
	scanf("%d", &cas);
	while(cas--) {
		FF(i, 4)
			scanf("%s", Map[i]);
		int ans = solve();
		printf("Case #%d: ", cas_c++);
		if(ans == 1)
			puts("X won");
		else if(ans == -1)
			puts("O won");
		else if(!ans)
			puts("Draw");
		else
			puts("Game has not completed");
	}
    return 0;
}




