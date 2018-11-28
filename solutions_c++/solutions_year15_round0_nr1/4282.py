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
		ll n,i,ans=0,res,cnt=0;
		sn(n);
		char str[n+2],*b,*e;
		ss(str);
		i=0;
		reps(b,e,n+1,str)
		{
			res=(int)*b%48;
			if((res>0)&&(cnt<i))
			{
				ans=ans+i-cnt;
				cnt=res+i;
			}
			else if(res>0)
			{
				cnt=cnt+res;
			}
			i++;
		}
		printf("Case #%lld: %lld\n",k,ans);
		k++;
	}
	return 0;
}