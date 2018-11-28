#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll k,c,s,tt,t;
	scanf("%lld",&tt);
	t=0;
	while(t!=tt)
	{
	t++;
	scanf("%lld %lld %lld",&k,&c,&s);
	
	printf("Case #%lld: ",t);
	for(ll i=1;i<=s;i++)
	printf("%lld ",i);
	printf("\n");
	
	}
	return 0;
}