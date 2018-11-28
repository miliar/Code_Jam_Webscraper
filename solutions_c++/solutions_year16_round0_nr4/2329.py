/*    SHUBHAM SINHA    */



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

ll power(ll a,ll b)
{
	ll x=1,y=a;
	while(b>0)
	{
		if(b%2)
			x=(x*y);
		y=(y*y);
		b=b/2;
	}
	return x;
}

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("D-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    ll t,k,c,s,i,p,tc=1;
    scanf("%lld",&t);
    while(t--)
    {
    	scanf("%lld%lld%lld",&k,&c,&s);
    	p=power(k,c-1);
    	printf("Case #%lld: ",tc);
    	for(i=0;i<k;i++)
    	{
    		if(i==0)
    			printf("1 ");
    		else
    			printf("%lld ",p*i+1);
    	}
    	printf("\n");
    	tc++;
    }
    return 0;
}