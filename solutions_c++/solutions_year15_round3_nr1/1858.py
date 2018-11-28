#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<map>
#include<algorithm>
#include<limits.h>
#include<set>
#include<stack>
#include<list>
#include<queue>
#include<math.h>
 
using namespace std;
#define lli long long int
#define ulli unsigned long long int
#define in(t) scanf("%d",&t)
#define inlf(t) scanf("%lf",&t)
#define inl(t) scanf("%ld",&t)
#define inll(t) scanf("%lld",&t)
#define inlu(t) scanf("%llu",&t)
#define MOD 1000000007
 
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("A-small-attempt0 (1).out","w",stdout);
    #endif
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    int t,i,r,c,w,j,cases,ans;
    cin>>t;
    for(cases=1;cases<=t;cases++)
    {
    	ans=0;
    	cin>>r>>c>>w;
    	if(w==1)
    	ans=c;
    	else if(w==c)
    	ans=w;
    	else
    	{
    		for(i=2;i<=5;i++)
    		{
    			if(c%i==0)
    			{
    				if(w>=(c/i))
    				{
    					ans=w+i-1;
    					break;
    				}
				}
				else
				{
					if(w>c/i)
					{
						ans=w+i-1;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<cases<<": "<<ans<<"\n";
	}
	return 0;
}
