#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 105
using namespace std;
typedef long long LL;
int t,n,m,ans,cx[M],cy[M];
char in[M][M];
bool fail;
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		scanf("%d %d",&n,&m);
		REP(i,1,n)scanf("%s",in[i]+1);

		MSET(cx,0);
		MSET(cy,0);
		REP(i,1,n)REP(j,1,m)
		{
			if(in[i][j]!='.') cx[i]++, cy[j]++;
		}

		ans = 0;
		fail = false;
		REP(i,1,n)REP(j,1,m)
		{
			bool flg1=false;
			if(i==1 || j==1 || i==n || j==m)
			{
				     if(i==1 && in[i][j]=='^') { ans++; flg1=true; }
				else if(i==n && in[i][j]=='v') { ans++; flg1=true; }
				else if(j==1 && in[i][j]=='<') { ans++; flg1=true; }
				else if(j==m && in[i][j]=='>') { ans++; flg1=true; }
			}
			//else
			//{
				int dx=0, dy=0;
				if(in[i][j]=='^') dx=-1;
				if(in[i][j]=='v') dx=1;
				if(in[i][j]=='<') dy=-1;
				if(in[i][j]=='>') dy=1;

				if(dx==0 && dy==0) continue;

				int x=i+dx, y=j+dy;
				bool flg=false;
				while(x>=1 && x<=n && y>=1 && y<=m)
				{
					if(in[x][y]!='.') flg = true;
					x += dx;
					y += dy;
				}

				if(!flg && !flg1) ans++;
				if(cx[i]<=1 && cy[j]<=1) fail = true;
			//}
		}

		printf("Case #%d: ",tt);
		if(fail) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}

