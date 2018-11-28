/*************************************
**----------------------------------**
*|**********************************|*
*|*  CODE By : Mohd. Ausaf Jafri   *|*
*|*     ECE, MNNIT , Allahabad     *|*
*|*                                *|*
*|*      ausafjafri@gmail.com      *|*
*|*   "Think Twice, Code Once"     *|*
*|**********************************|*
**----------------------------------**
**************************************/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define vi(v,size) vector<int>v(size) 
#define upto(n) for(int i=0;i<n;i++)
#define from(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define mp make_pair
#define pb push_back
#define mod 1000000007

#define inc(c) scanf("%c",&c);
#define ins(s) scanf("%s",s);
#define ind(n) scanf("%d",&n);
#define inlld(n) scanf("%lld",&n);
#define ind2(n,m) scanf("%d%d",&n,&m);
#define inlld2(n,m) scanf("%lld%lld",&n,&m);

#define opc(c) printf("%c\n",c);
#define ops(s) printf("%s\n",s);
#define opd(n) printf("%d\n",n);
#define oplld(n) printf("%lld\n",n);
#define opd2(n,m) printf("%d %d\n",n,m);
#define oplld2(n,m) printf("%lld %lld\n",n,m);

ll tobinary(ll n)
{
    ll res=0;
    while(n>0)
    {
        res=res*10+(n%2);
        n=n/2;
    }
    ll temp=res;
    res=0;
    while(temp)
    {
        res=res*10 + (temp%10);
        temp=temp/10;
    }
    return res;
}
ll power(ll a,ll b)
{
    ll res=1;
    while(b>0)
    {
        if(b%2==1)
            res=res*a;
        b=b>>1;
        a=a*a;
    }
    return res;
}
ll tobase(ll n,int base)
{
    ll res=0,i=0;
    while(n)
    {
        if(n%10)
        res=res+power((ll)base,i);
        n=n/10;
        i++;
    }
    return res;
}

ll notprime(ll n)
{
    for(ll i=2;i*i<n;i++)
    {
        if(n%i==0)
         return i;
    }
    return 0;
}
int main()
{
    int tt,n,j,count=0;
    ind(tt)
    ind2(n,j)
    ll i,l,u;
    l=(1<<15);
    u=(1<<16);
    ops("Case #1:")
    for(i=l+1;i<u;i=i+2)
    {
            ll base[20],flag=1,divisor[20];
            //oplld(i)
            base[2]=i;
            base[10]=tobinary(i);
            //oplld(base[10])
            for(int j=3;j<=9;j++)
            base[j]=tobase(base[10],j);
            //ops("hello")
            for(int t=2;t<=10;t++)
            {
                
                divisor[t]=notprime(base[t]);
                if(!divisor[t])
                {
                    flag=0;
                    break;
                }
            }
            if(count < 50)
            {
             if(flag)
             {
                 count++;
                 
                 printf("%lld",base[10]);
                 for(int j=2;j<=10;j++)
                     printf(" %lld",divisor[j]);
                 
                 printf("\n");
                 //     for(int j=2;j<10;j++)
               //      printf("%lld ",base[j]);
                 //printf("\n");
                 
             }
            }
            else
                exit(0);
    }
   
    
}