/*
author : lifecodemohit
*/
 
#include <bits/stdc++.h>
using namespace std;
 
#define ll long long int
#define MOD 1000000007
#define sn(n) scanf("%lld",&n)
#define pn(n) printf("%lld\n",n)
#define ss(str) scanf("%s",str)
#define ps(str) printf("%s\n",str)
#define rep(i,s,e) for(i=s;i<=e;i++)
#define reprev(i,s,e) for(i=s;i>=e;i--)
#define reps(b,e,g,str) for(b=str,e=&str[g-1];b<=e;b++) 
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define dis(arr,s,e) for(i=s;i<=e;i++) printf("%lld ",arr[i]); printf("\n"); 

int main()
{
	ll T,k=1;
	sn(T);
	while(T--)
	{
		ll x,r,c,mini,maxi,res;
		sn(x);
		sn(r);
		sn(c);
		mini=min(r,c);
		maxi=max(r,c);
		res=r*c;
		if(x==1)
		{
			printf("Case #%lld: GABRIEL\n",k);
		}
		else if(x==2)
		{
			if(mini>=1&&maxi>=2&&(res%2==0))
			{
				printf("Case #%lld: GABRIEL\n",k);
			}
			else
				printf("Case #%lld: RICHARD\n",k);
		}
		else if(x==3)
		{
			if(mini>=2&&maxi>=3&&(res%3==0))
			{
				printf("Case #%lld: GABRIEL\n",k);
			}
			else
				printf("Case #%lld: RICHARD\n",k);	
		}
		else if(x==4)
		{
			if(mini>=3&&maxi>=4&&(res%4==0))
			{
				printf("Case #%lld: GABRIEL\n",k);
			}
			else
				printf("Case #%lld: RICHARD\n",k);	
		}
		k++;
	}
	return 0;
}