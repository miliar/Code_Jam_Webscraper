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
ll N,pj=0,j,pm;
ll primenums[47000];
void genPrime()
{
    int k=0;
    primenums[k++]=2;
    for(int n=3;n<47000;n=n+2){
        int flag=0;
        for(int i=3;i<=sqrt(n);i++)
        {
            if(n%i==0){
                flag=1;
                break;
            }
        }
        if(flag==0)
            primenums[k++]=n;
    }
    pm=k;//to get max index of primes
}
int isPrime(ll n)
{
    for(int i=0;i<pm&&primenums[i]<=sqrt(n);i++)
    {
        if(n%primenums[i]==0)
            return primenums[i];
    }
    return 0;
}
struct node
{
    ll a[35];
};
void rec(ll n,struct node Node)
{
    if(n<N-1)
    {
      //  pi(4444);pnl;
        struct node newNode ;
        newNode = Node ;
        newNode.a[n]=1;
       /* repi(N)
    {
        pi(Node.a[i]);ps;
    }pnl;*/
   /* repi(N)
    {
        pi(newNode.a[i]);ps;
    }pnl;*/
                ll count=0;
            ll prime[11];
           /* for(int base=2;base<=10;base++)
            {
                ll num=0,k=1;
                repi(n)
                {
                    num=num+pow(base,n-k)*Node.a[i];

                }
                prime[base]=num;
                if(isPrime(num))
                    count++;
            }
            if(pj<j){
            if(count==0)
            {
                repi(n)
                pi(Node.a[i]);
                ps;
                for(int i=2;i<=10;i++)
                {
                    pl(prime[i]);ps;
                }pnl;
                pj++;
            }rec(n+1,Node);
            }
            else
            {
                return ;
            }*/
            //for newNode
              count=0;
            
            for(int base=2;base<=10;base++)
            {
                         ll num=0,k=0;
                for(int i=N-1;i>=0;i--)
                {
                    num=num+pow(base,k++)*newNode.a[i];

                }
               //  pi(num);ps;
                int nontrifact=isPrime(num);
              //  pi(nontrifact);pnl;
                prime[base]=nontrifact;
                if(nontrifact==0)
                    count++;
            }//pnl;
            newNode.a[0]=1;
            if(pj<j){
            if(count==0)
            {
                repi(N)
                pi(newNode.a[i]);
                ps;
                for(int i=2;i<=10;i++)
                {
                    pl(prime[i]);ps;
                }pnl;
                pj++;
            }rec(n+1,newNode);rec(n+1,Node);
            }
            else
            {
                return ;
            }
    }
    return;
}
int main(void)
{
    ll t;
    sl(t);
    while(t--){
 ll n;
 sl(n);sl(j);
 N=n;
  struct node Node;
    printf("Case #1:");pnl;
    memset(Node.a,0,sizeof(int)*35);
    Node.a[0]=1;Node.a[n-1]=1;
    ll count=0;
    ll prime[11];
    genPrime();
    /*repi(11)
    {
        pi(primenums[i]);ps;
    }pnl;
    repi(n)
    {
        pi(Node.a[i]);ps;
    }pnl;*/
    for(int base=2;base<=10;base++)
    {
       // pi(111);pnl;
        ll num=0,k=0;
        for(int i=N-1;i>=0;i--)
        {
            num=num+pow(base,k++)*Node.a[i];

        }
       // pi(num);ps;
         int nontrifact=isPrime(num);
       //  pi(nontrifact);pnl;
                prime[base]=nontrifact;
                if(nontrifact==0)
                    count++;
    }
   // pnl;
    Node.a[0]=1;
 /*repi(n)
    {
        pi(Node.a[i]);ps;
    }pnl;*/
   // pi(pj);ps;pi(j);pnl;
    if(pj<j){
        // pi(222);pnl;
    if(count==0)
    {
         //pi(222);pnl;
        repi(N)
        pi(Node.a[i]);
        ps;
        for(int i=2;i<=10;i++)
        {
            pl(prime[i]);ps;
        }pnl;
        pj++;
    }
    
    rec(1,Node);
    }
}
 return 0;
}