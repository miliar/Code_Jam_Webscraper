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
#define M 1005
using namespace std;
typedef long long LL;
int t,n,ans1,ans2,l,r;
double in1[M],in2[M];
bool vis[M],flag;

int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		MSET(vis,false);
		scanf("%d",&n);
		REP(i,1,n)scanf("%lf",&in1[i]);sort(in1+1,in1+1+n);
		REP(i,1,n)scanf("%lf",&in2[i]);sort(in2+1,in2+1+n);

		ans1=ans2=0;
		l=1;r=n;
		REP(i,1,n)
		{
			if(in1[i] > in2[l])
			{
				ans1++;
				l++;
			}
			else
			{
				r--;
			}
		}

		REP(i,1,n)
		{
			flag=false;
			REP(j,1,n)if(!vis[j] && in2[j]>in1[i])
			{
				vis[j]=true;
				flag=true;
				break;
			}

			if(!flag)
			{
				ans2++;
				REP(j,1,n)if(!vis[j])
				{
					vis[j]=true;
					break;
				}
			}
		}

		printf("Case #%d: %d %d\n",tt,ans1,ans2);
	}
	return 0;
}

