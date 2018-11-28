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
#define maxN 100
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

char a[maxN+5];

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("B-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    ll t,i,j,n,z,ans,tc=1;
    scanf("%lld",&t);
    while(t--)
    {
    	scanf("%s",a);
    	n=strlen(a);
    	ans=0;
    	z=-1;
    	for(i=0;i<n;i++)
    	{
    		if(z==1)
    			ans=ans+1;
    		if(a[i]=='+')
    			z=1;
    		else
    			z=0;
    		j=i;
    		while(j<n&&a[j]==a[i])
    			j++;
    		if(z==0)
    			ans=ans+1;
    		i=j-1;
    	}
    	printf("Case #%lld: %lld\n",tc++,ans);
    }
    return 0;
}