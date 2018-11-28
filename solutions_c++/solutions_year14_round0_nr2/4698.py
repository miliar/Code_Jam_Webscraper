#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<iomanip>
#define getcx getchar_unlocked
#ifndef ONLINE_JUDGE
    #define getcx getchar
#endif
#define mod 1000000007
#define l long long
using namespace std;
inline int inp()
{
   int n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   return n*sign;
}
inline long long in()
{
   long long n=0;
   long long ch=getcx();long long sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )

   return n*sign;
}
main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t;
    float c,f,x,a,b;
    cin>>t;
    for(int z=1;z<=t;++z)
    {
        cin>>c>>f>>x;
        a=x/2.0;
        b=(c/2.0)+(x/(2.0+f));
        for(int i=2;(a-b)>0.0000001;++i)
        {
            a=b;
            b=0.0;
            for(int j=0;j<i;++j)
            {
                b+=(c/((f*(float)j)+2.0));
            //    cout<<fixed<<setprecision(7)<<(c/((f*(float)j)+2.0))<<" ";
            }
            b+=(x/((f*(float)i)+2.0));
            //cout<<fixed<<setprecision(7)<<b<<" "<<endl;
        }
            cout<<"Case #"<<z<<": "<<fixed<<setprecision(7)<<a<<endl;
    }
}
