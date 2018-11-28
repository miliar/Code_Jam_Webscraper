#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000

bool vis[20];
int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	ll t,tcase,k,c,s,i;
	scanf("%lld",&tcase);
	for(t=1;t<=tcase;t++)
	{
	   scanf("%lld %lld %lld",&k,&c,&s);
	   printf("Case #%d: ",t);
	   for(i=1;i<=k;i++)
	   {
	   	 printf("%lld ",i);
	   }
	   printf("\n");
	}
	
	
}

