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
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int t,count1,a[5][5],b[5],c[5],ans,n;
    cin>>t;
    for(int z=1;z<=t;++z)
    {
        cin>>n;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
                cin>>a[i][j];
        }
        for(int i=0;i<4;++i)
            b[i]=a[n-1][i];
        cin>>n;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
                cin>>a[i][j];
        }
        for(int i=0;i<4;++i)
            c[i]=a[n-1][i];
            count1=0;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(c[i]==b[j])
                {
                    ++count1;
                    ans=c[i];
                }
            }
        }
        if(count1==0)
            cout<<"Case #"<<z<<": Volunteer cheated!\n";
        else if(count1==1)
            cout<<"Case #"<<z<<": "<<ans<<endl;
        else
            cout<<"Case #"<<z<<": Bad magician!\n";

    }
}
