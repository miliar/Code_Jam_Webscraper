//azariamuh

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
using namespace std;

int inf = 1000000000;
typedef long long LL;

#define forn(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define reset(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()

int T,r,c;
char in[105][105];
int dirx[] = {0,0,1,-1};
int diry[] = {1,-1,0,0};

bool tabrak(int x,int y,int dir) {
	for (int i = 1; ; ++i) {
		int xx = x + dirx[dir] * i;
		int yy = y + diry[dir] * i;
		if (0 <= xx && xx < r && 0 <= yy && yy < c);
		else return false;
		if (in[xx][yy] != '.') return true;
	}
}

int main()
{
	scanf("%d",&T);
	forn(cases,1,T)
	{
		printf("Case #%d: ",cases);
		scanf("%d %d",&r,&c);
		forn(i,0,r-1) scanf("%s",in[i]);
		int ans = 0;
		bool bisa = 1;
		forn(i,0,r-1) forn(j,0,c-1) if (in[i][j] != '.') {
			if (!bisa) break;
			int dir = -1;
			if (in[i][j] == '^') dir = 3;
			if (in[i][j] == 'v') dir = 2;
			if (in[i][j] == '>') dir = 0;
			if (in[i][j] == '<') dir = 1;
			if (tabrak(i,j,dir)) continue;
			bool ok = 0;
			forn(k,0,3) if(tabrak(i,j,k)) {
				++ans;
				ok = 1;
				break;
			}
			if (!ok) {
				puts("IMPOSSIBLE");
				bisa = 0;
				break;
			}
		}
		if (bisa) printf("%d\n",ans);
	}
	return 0;
}













