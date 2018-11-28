#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
int main()
{
	ll int i,j,k,c,s,l;
	ll int t;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	slld(t);
	for(i=1;i<=t;i++)
	{
		slld(k);
		slld(c);
		slld(s);
		j=1;
		if(k!=1)
		{
			while(c--)
			{
				j=j*k;
			}
			j--;
			printf("Case #%lld: ",i);
			j=j/(k-1);

		for(k=0;k<=s-1;k++)
		{
			printf("%lld ",j*k+1 );
		}
		printf("\n");
		}
		else
			printf("Case #%lld: 1\n",i);
	}
	return 0;
}