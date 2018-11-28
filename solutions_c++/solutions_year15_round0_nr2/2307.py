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
	freopen("B-large.in","r",stdin);
	freopen("B-L.txt","w",stdout);
	
    lli t,cse,d,i,j,ans,lim,maxi,cur;
    
	scanf("%lld",&t);
    
	for ( cse=1;cse<=t;cse++ )
    {
        lim = 0;
        
		scanf("%lld",&d);
		lli a[1001];
		
        for ( i=1;i<=d;i++ )
        {
            scanf("%lld",&a[i]);
            lim = (lim>a[i])?lim:a[i];
        }
		
        ans = lim;
        for ( i=1;i<=lim;i++ )
        {
            cur = maxi = 0;
            for ( j=1;j<=d;j++ )
            {
                if ( a[j]>i )
                {
                    cur += (a[j]/i)+((a[j]%i==0)?0:1) - 1;
                    maxi = (maxi>i)?maxi:i;
                }
                else 
					maxi = (maxi>a[j])?maxi:a[j];
            }
			
            cur += maxi;
			
            if ( cur<ans )
				ans = cur;
        }
        printf("Case #%lld: %lld\n",cse,ans);
    }
    return 0;
}
