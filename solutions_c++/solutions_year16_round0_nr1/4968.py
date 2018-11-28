#include <bits/stdc++.h>
#define ll long long
using namespace std;
bool h[10];
ll int mc;
void myfind(ll int x)
{
	char str[50];
	sprintf(str,"%lld",x);
	ll int i,l;
	l=strlen(str);
	for(i=0;i<l;i++)
	{
		if(h[str[i]-'0']==0)
		{
			h[str[i]-'0']=1;
			mc++;
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll int test,t;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		memset(h,0,sizeof(h));
		ll int n;
		cin>>n;
		ll int i,ans;
		mc=0;
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",t);
		}
		else
		{
			for(i=1;;i++)
			{
				myfind(n*i);
				if(mc==10)
				{
					ans=n*i;
					break;
				}
			}
			printf("Case #%lld: %lld\n",t,ans);
		}
	}
	return 0;
}
