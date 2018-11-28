// author:Nitesh Singh Thapar University
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#define getcx getchar_unlocked
#ifndef ONLINE_JUDGE
    #define getcx getchar
#endif
using namespace std;
#define ull unsigned long long int
#define lli long long int
#define li long int
#define ii int
#define mod 1000000007


inline int intp()
{
   int n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   return n*sign;
}

inline long long llip()
{
   long long n=0;
   long long ch=getcx();long long sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   return n*sign;
}
int main()
{
   // freopen("standing.in","r",stdin);
  //freopen("standing.out","w",stdout);
    int t;
    t = intp();
    int cs=1;
    while(cs<=t)
    {
        printf("Case #%d: ",cs),cs++;
        //s = ip();
        short a[1001],smax=0;
        string s;
        int ppl=0;
        smax = intp();
        cin>>s;
        int len = s.length();
        int l=0;
        a[l]=int(s[l])-'0';
        int stand=a[l];
        l++;
        while(l<len && stand<smax)
        {
            a[l]=int(s[l])-'0';
            if(stand<l)
               {
                 ppl=ppl+(l-stand);
                stand=stand+a[l]+l-stand;
               // cout<<" l="<<l<<"ppl="<<ppl<<" ";
               }
            else
                {
                    stand=stand+a[l];
           // cout<<" l="<<l<<"stand="<<stand<<" ";
                }
            l++;

        }
        cout<<ppl;
        if(cs<=t)
            ppl=0;
        cout<<"\n";
    }
    return 0;
}
