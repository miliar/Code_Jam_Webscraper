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
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    #endif
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    int t,i,smax,l,j,cases;
    lli ans,count;
    string s;
    cin>>t;
    for(cases=1;cases<=t;cases++)
    {
    	ans=count=0;
    	cin>>smax>>s;
    	l=s.length();
		for(i=0;i<l;i++)
		{
			int temp=s[i]-48;
			for(j=0;j<temp;j++)
			{
				if(i==0)
				count++;
				else
				{
					if(count>=i)
					count++;
					else
					{
						ans+=i-count;
						count+=i-count;
						count++;
					}
				}
			}
		}
		cout<<"Case #"<<cases<<": "<<ans<<"\n";
	}
	return 0;
} 
