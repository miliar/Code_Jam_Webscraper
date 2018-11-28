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
void del(float a[],int n,int pos)
{
    for(int i=pos;i<n-1;++i)
    a[i]=a[i+1];
}
main()
{
   // freopen("D-large.in","r",stdin);
    //freopen("D-large.out","w",stdout);
    int t,nao,n1,ken,nao1,ken1,n;
    bool flag;
    float a[1001],b[1001],c[1001];
    cin>>t;
    for(int z=1;z<=t;++z)
    {
        nao1=0;
        ken1=0;
        nao=0;
        ken=0;
        cin>>n;
        for(int i=0;i<n;++i)
            cin>>a[i];
        for(int j=0;j<n;++j)
        {
            cin>>b[j];
            c[j]=b[j];
        }
        sort(b,b+n);
        n1=n;
        for(int i=0;i<n;++i)
        {
            flag=0;
            for(int j=0;j<n1;++j)
            {
                if(b[j]>a[i])
                {
                    del(b,n1,j);
                    ++ken;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                del(b,n,0);
                ++nao;
            }
            --n1;
        }
        sort(c,c+n);
        sort(a,a+n);
        n1=n;
        for(int i=0;i<n;++i)
        {
            flag=0;
            for(int j=0;j<n1;++j)
            {
                if(a[j]>c[i])
                {
                    del(a,n1,j);
                    ++nao1;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                del(a,n,0);
                ++ken1;
            }
            --n1;
        }
        cout<<"Case #"<<z<<": "<<nao1<<" "<<nao<<endl;
    }
}
