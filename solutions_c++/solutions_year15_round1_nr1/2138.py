#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
#define clear(a) memset((a),0,sizeof(a))
#define pb push_back
#define SIZE(v) v.size()
#define ull unsigned long long int
#define lli long long int
#define li long int
#define ii int
#define mod 1000000007
/* Created by : Rahul Johari
				Thapar University */
				
int main()
{
    lli t,cse,n,i,min1,min2,maxi;
    
	freopen("A-large.in","r",stdin);
    freopen("A-L.txt","w",stdout);

    scanf("%lld",&t);
	
    for ( cse=1;cse<=t;cse++ )
	{
        scanf("%lld",&n);
        
		lli a[n+1];
        
		for ( i=0;i<n;i++ )
            scanf("%lld",&a[i]);
        
		min1 = min2 = maxi = 0;
        
		for ( i=1;i<n;i++ )
		{
            if ( a[i]-a[i-1]<0 ) 
                min1 += a[i-1] - a[i];
				
            maxi = (maxi>(a[i-1]-a[i]))?maxi:(a[i-1]-a[i]);
        }
        for ( i=0;i<n-1;i++ )
		{
            if ( a[i]>=maxi )
				min2 += maxi;
            else 
				min2 += a[i];
        }
        printf("Case #%lld: %lld %lld\n",cse,min1,min2);
    }
    return 0;
}
