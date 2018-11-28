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
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    #endif
    //ios_base::sync_with_stdio(false); cin.tie(0);
    
    int t,i,x,r,c,cases;
    string s;
    cin>>t;
    for(cases=1;cases<=t;cases++)
    {
    	s="";
    	cin>>x>>r>>c;
    	if(x==1)
    	s="GABRIEL";
    	
    	else if(x==2)
    	{
    		if((r*c)%2==0)
    		s="GABRIEL";
    		else
    		s="RICHARD";
		}
		
		else if(x==3)
		{
			if(r==1)
			{
    			s="RICHARD";
			}
			else if(r==2)
			{
				if(c==3)
				s="GABRIEL";
    			else
    			s="RICHARD";
			}
			else if(r==3)
			{
				if(c==1)
				s="RICHARD";
				else
				s="GABRIEL";
			}
			else if(r==4)
			{
				if(c==3)
				s="GABRIEL";
    			else
    			s="RICHARD";
			}
		}
		
		else if(x==4)
		{
			if(r==1)
			{
    			s="RICHARD";
			}
			else if(r==2)
			{
    			s="RICHARD";
			}
			else if(r==3)
			{
				if(c==4)
				s="GABRIEL";
    			else
    			s="RICHARD";
			}
			else if(r==4)
			{
				if(c>2)
				s="GABRIEL";
    			else
    			s="RICHARD";
			}
		}
		cout<<"Case #"<<cases<<": "<<s<<"\n";
	}
	return 0;
}
