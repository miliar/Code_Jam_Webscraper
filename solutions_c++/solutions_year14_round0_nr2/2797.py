#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

//#define SMALL
#define LARGE

int main()
{

	#ifdef SMALL
		freopen("B-small-attempt2.in","rt",stdin);
		freopen("B-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		long double ans=0,ctime,ntime;
		long double c,f,x,cookies=2;
		int j;
		cin>>c>>f>>x;		
		
		while(true)
		{
			ctime=x/cookies;
			ntime=(c/cookies)+(x/(cookies+f));
			if(ctime<=ntime)
			{
				ans+=ctime;
				break;
			}
			else
			{
				ans=ans+(c/cookies);
				cookies+=f;
			}
		}	
		
		printf("Case #%d: %.7Lf\n",i,ans);		
	}
	
	return 0;
}
