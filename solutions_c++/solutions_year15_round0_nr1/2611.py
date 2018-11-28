/*
*************************************************************************
* $ Author : honeyslawyer   $
* $ Name   : shashank gupta $
*************************************************************************
*
* Copyright 2014 @ honeyslawyer and shashank gupta
*
************************************************************************/
#include<cstdio>
#include<iostream>
#include<cmath>
#include<conio.h>
#include<cstring>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<string>
#include<climits>

#define mod 1000000007
#define ll long long

using namespace std;
ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m)
 {ll ans=1;
  b%=m;
  while(exp)
   {if(exp&1)
     ans=(ans*b)%m;
    exp>>=1;
	b=(b*b)%m;
   }
  return ans;
 }

int main()
{
    int t;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int smax;
        cin>>smax;
        string s;
        cin>>s;
        int ans=0;
        int count=s[0]-'0';
        for(int i=1;i<s.size();i++)
        {
            if(count>=i)
            {
                count=count+(s[i]-'0');
            }
            else if(s[i]>0)
            {
                ans=ans+(i-count);
                count=i+s[i]-'0';
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }






getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
