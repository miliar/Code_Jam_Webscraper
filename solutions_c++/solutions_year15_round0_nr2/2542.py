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
map<int,int> m;
int check(int x,int q)
{
    map<int,int> b;
    for(map<int,int> :: iterator it=m.begin();it!=m.end();it++)
    {
        b[it->first]=it->second;
    }
    map<int,int> :: iterator it=b.end();
    it--;
    int mx=it->first;
    while(x<it->first&&x>0)
    {
        //cout<<mx<<endl;
        x--;
        b[mx]--;
        if(mx%2==1&&mx%3==0&&q)
        {
            {
                b[(mx/6+1)*3]++;
                b[(mx/6)*3]++;
            }
        }
        else if(mx%2==0)
        {
            b[mx/2]+=2;
        }
        else
        {
            b[mx/2+1]++;
            b[mx/2]++;
        }
        if(b[mx]==0)
        {
            b.erase(b.find(mx));
        }
        it=b.end();
        it--;
        mx=it->first;
        if(mx==1&&x>=1)
        return true;
    }
    if(x>0)
    return true;
    else
    return false;

}
int main()
{
    int t;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int d;
        int a[2000];
        cin>>d;
        int mx=-1;
        m.clear();
        for(int i=0;i<d;i++)
        {
            cin>>a[i];
            m[a[i]]++;
            mx=max(mx,a[i]);
        }
        int l=0,h=mx+10;
        int ans=mx+1000;
        while(l<=h)
        {
            int mid=l+(h-l)/2;
            if(check(mid,0))
            {
                ans=min(ans,mid);
                h=mid-1;
            }
            else
            l=mid+1;
        }
        l=0,h=mx+10;
        while(l<=h)
        {
            int mid=l+(h-l)/2;
            if(check(mid,1))
            {
                ans=min(ans,mid);
                h=mid-1;
            }
            else
            l=mid+1;
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
        
        

    }
    






getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
