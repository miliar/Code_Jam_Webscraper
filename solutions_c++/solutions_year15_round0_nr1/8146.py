#include<bits/stdc++.h>
#define SI(n) scanf("%d",&n)
#define SII(a,b) scanf("%d%d",&a,&b)
#define SIII(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SLL(n) scanf("%lld",&n)
#define SC(r) scanf("%c",&r)
#define SS(r) scanf("%s",r)
#define REPA(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define PI(n) printf("%d\n",n)
#define PII(a,b) printf("%d %d\n",a,b)
#define PLL(n) printf("%lld\n",n)
#define PC(n) printf("%c\n",n)
#define PS(n) printf("%s\n",n)
#define ll long long
#define pb push_back
#define mp make_pair
#define M 1000000007

using namespace std;

int main()
{
	int T;

	SI(T);
	
	int sm;
	char x;
	int cs=0;
	while(T--)
	{
		cs++;
		SI(sm);
		int ans=0;
		int cur=0;
		int inp;
		getchar();
		REP(i,sm+1)
		{
			x=getchar();
			inp=(int)(x-'0');

			if(inp!=0)
			{
				if(cur < i)
				{
					ans+=(i-cur);
					cur=i;
				}
				cur+=inp;
			}
		}
		printf("Case #%d: ",cs);
		PI(ans);
	}

	return 0;
}
