/* 

   SHUBHAM RAI-IIIT Hyderabad

 */
#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<climits>
#include<string>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) for(i=0;i<a;i++)
#define LLD long long int
#define MOD 1000000007
#define si(n) scanf("%d",&n);
#define si2(n,m) scanf("%d%d",&n,&m);
#define sl(n) scanf("%lld",&n);
#define F first
#define S second
typedef pair<int,int> PII;
int main()
{
	int test,t;
	si(test);
	for(t=1;t<=test;t++)	
	{
		int ans1,ans2,f[17]={0},i,j,x;
		si(ans1);
		REP(i,4)
		{
			REP(j,4)
			{
				si(x);
				if(i+1==ans1)
					f[x]++;
			}
		}
		si(ans2);
		REP(i,4)
		{
			REP(j,4)
			{
				si(x);
				if(i+1==ans2)
					f[x]++;
			}
		}
		int c2=0,ans=0;
		FOR(i,1,17)
		{
			if(f[i]==2)
			{
				c2++;
				ans=i;
			}
		}
		if(c2==1)
			printf("Case #%d: %d\n",t,ans);
		else if(c2>1)
			printf("Case #%d: Bad magician!\n",t);
		else
			printf("Case #%d: Volunteer cheated!\n",t);
	}
	return 0;
}
