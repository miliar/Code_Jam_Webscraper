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
#define M 
using namespace std;
typedef long long LL;
int t,r[2],cnt,ans;
int in[2][5][5];
bool vis[2][20];
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		MSET(vis,false);
		scanf("%d",&r[0]);
		REP(i,1,4)REP(j,1,4)scanf("%d",&in[0][i][j]);
		scanf("%d",&r[1]);
		REP(i,1,4)REP(j,1,4)scanf("%d",&in[1][i][j]);

		REP(i,0,1)REP(j,1,4)vis[i][ in[i][r[i]][j] ] = true;

		cnt=0;
		REP(i,1,16)if(vis[0][i] && vis[1][i])
		{
			ans=i;
			cnt++;
		}

		printf("Case #%d: ",tt);
		if(cnt>1)puts("Bad magician!");
		else if(cnt==0)puts("Volunteer cheated!");
		else printf("%d\n",ans);
	}
	return 0;
}

