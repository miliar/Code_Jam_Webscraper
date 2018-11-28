#include<iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<utility>
#include<cstring>
#include <list>
using namespace std;
#define ll long long int
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sc(x) scanf("%c",&x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld",x)
#define pnl printf("\n")
#define ps printf(" ")

#define repi(n) for(ll i=0;i<n;i++)
#define repj(n) for(ll j=0;j<n;j++)
#define fr(m,n) for(ll i=m;i<=n;i++)
#define gc getchar_unlocked
  #define pc(x) putchar_unlocked(x);
    inline void writeInt (int n)
    {
        int N = n, rev, count = 0;
        rev = N;
        if (N == 0) { pc('0'); pc('\n'); return ;}
        while ((rev % 10) == 0) { count++; rev /= 10;} //obtain the count of the number of 0s
        rev = 0;
        while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}  //store reverse of N in rev
        while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
        while (count--) pc('0');
    }
void inline fastfunction(int *x)
{
    register int c = gc();
    *x = 0;
    for( ;(c < 48 || c > 57); c = gc())
        ;
    for( ;c > 47 && c < 58; c = gc())
    {
        *x = ( *x << 1 ) + ( *x << 3 ) + c - 48;
    }
}
int a[10];
int check()
{
 repi(10)
   if(a[i]==0)
    return 0;
 return 1;
}
int main(void)
{
 ll t;
 sl(t);
 int k=t;
 while(t--)
 {
 	ll n;
    sl(n);
    memset(a,0,sizeof(int)*10);
    ll i=0;
    ll N=n;
    if(n!=0)
    {
    do
    {
        i++;
        n = N*(i);
        ll x = n;
        while(x)
        {
            ll r = x%10;
            x = x/10;
            a[r]++;
        }
        /*repi(10)
        {
            pi(a[i]);ps;
        }pi(n);pnl;*/
     }while(!check());
  /*  if(i>sqrt(N))
    {
        printf("Case #%d: INSOMNIA",k-t);pnl;
    }
    else*/
        printf("Case #%d: ",k-t);pi(n);pnl;
    }
    else
    {
        printf("Case #%d: INSOMNIA",k-t);pnl;
    }

 }
 return 0;
}