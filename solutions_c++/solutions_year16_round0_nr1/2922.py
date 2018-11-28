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

map<ll,ll> m;

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    ll t,n,visit,z,p,x,c,tc=1;
    scanf("%lld",&t);
    while(t--)
    {
    	scanf("%lld",&n);
    	m.clear();
    	visit=0;
    	z=0;
    	c=1;
    	while(true)
    	{
    		if(visit==1023)
    		{
    			z=1;
    			break;
    		}
    		p=n*c;
    		if(m[p])
    			break;
    		m[p]=1;
    		while(p>0)
    		{
    			x=p%10;
    			if((visit&(1<<x))==0)
    				visit=(visit|(1<<x));
    			p=p/10;
    		}
    		c++;
    	}
    	if(z)
    	{
    		p=n*(c-1);
    		printf("Case #%lld: %lld\n",tc,p);
    	}
    	else
    		printf("Case #%lld: INSOMNIA\n",tc);
    	tc++;
    }
    return 0;
}