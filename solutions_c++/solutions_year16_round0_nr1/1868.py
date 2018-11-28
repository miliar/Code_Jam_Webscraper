#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
bool vis[11];
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	int t;
	ll n,i;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		sl(n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",tt);
			continue;
		}
		clr(vis);
		int cnt=0;
		for(i=1;;i++)
		{
			ll n1=i*n;
			if(n1==0)
			{
				if(!vis[0])
				{
					vis[0]=1;
					cnt++;
				}
			}
			while(n1)
			{
				int d=n1%10;
				n1/=10;
				if(!vis[d])
				{
					vis[d]=1;
					cnt++;
				}
			}
			if(cnt==10)
				break;
		}
		printf("Case #%d: %lld\n",tt,i*n);
	}
}