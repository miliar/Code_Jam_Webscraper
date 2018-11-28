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
        int x,ori,oc,r,c;
        cin>>x>>ori>>oc;
        if(x==1)
        cout<<"Case #"<<z<<": GABRIEL"<<endl;
        else if(x==2)
        {
            r=max(ori,oc);
            c=min(ori,oc);
            if(r%2==0||c%2==0)
            cout<<"Case #"<<z<<": GABRIEL"<<endl;
            else
            cout<<"Case #"<<z<<": RICHARD"<<endl;
        }
        else if(x==3)
        {
            r=max(ori,oc);
            c=min(ori,oc);
            if((r==3&&c==2)||(r==4&&c==3)||(r==3&&c==3))
            cout<<"Case #"<<z<<": GABRIEL"<<endl;
            else
            cout<<"Case #"<<z<<": RICHARD"<<endl;
        }
        else if(x==4)
        {
            r=max(ori,oc);
            c=min(ori,oc);
            if(r==4&&(c==3||c==4))
            cout<<"Case #"<<z<<": GABRIEL"<<endl;
            else
            cout<<"Case #"<<z<<": RICHARD"<<endl;

        }
        
    }






getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
