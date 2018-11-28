#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<string.h>
#include<cmath>
#include<iostream>
#include<vector>
#include<sstream>
#include <map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define piw(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plln(n) printf("%lld\n",n)
#define pllw(n) printf("%lld ",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define psn(s) printf("%s\n",s)
#define psw(s) printf("%s ",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")
#define NM 100005
#define inf 1000000007
typedef long long int ll;
using namespace std;

int a[10008];
int main()
{
    int t,m,n,i,j,k,l;
    
    cin>>t;
    int ct=1;
    while(t--)
    {
        cin>>n;
        
        for(i=1;i<=n;i++)
            cin>>a[i];
        
        int ans1=0,ans2=0;
        for(i=2;i<=n;i++)
        {
            int x=a[i]-a[i-1];
            if(x<0)
                ans1+=abs(x);
                
        }    
        int y=0.0;
        for(i=1;i<=n-1;i++)
        {
            int x=a[i+1]-a[i];
            if(x<0)
            {
                x=abs(x);
                y=max(x,y);
            }
        }
        
        for(i=2;i<=n;i++)
        {
            int x=a[i]-a[i-1];
            int z=y;
           
            
            if(x<0)
            {
                x=abs(x);
                ans2+=min(a[i-1],z);
            }
            else
                ans2+=min(a[i-1],z);
            //cout<<ans2<<" ";
        }
        
        cout<<"Case #"<<ct++<<": ";
        cout<<ans1<<" "<<ans2<<"\n";
        
    }    
    
}    
