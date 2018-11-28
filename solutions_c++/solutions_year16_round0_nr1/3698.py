#include<bits/stdc++.h>
//#include<iostream>
//#include<stdio.h>


using namespace std;

#define ll int
#define lll long long int
#define s(a) scanf("%d",&a)
#define slll(a) scanf("%lld",&a)
#define fr(i,n) for(i=0;i<n;i++)
#define fra(i,a,n) for(i=a;i<n;i++)
//#define N 100010
#define inf lll_MAX
#define MOD 1000000007
#define SET(v,i) memset(v, i, sizeof(v))

/*#define gc getchar_unlocked

void scanlll(lll &x)
{
    register lll c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

ll gcd(ll a,ll b)
{
   //cout<<a<<" "<<b<<endl;
   if(b==0)
   return a;
   return gcd(b,a%b);
}*/
/*
struct node
{
  ll rank0,rank1,pos;
};

bool cmp(node a,node b)
{
  if(a.rank0==b.rank0)
    return a.rank1<b.rank1;

  return a.rank0<b.rank0;
}*/
/*int cmpqsort (const void * a, const void * b)
{
  if(((node*)a)->rank0==((node*)b)->rank0)
    return ( ((node*)a)->rank1 - ((node*)b)->rank1 );

    return ( ((node*)a)->rank0 - ((node*)b)->rank0 );


}*/
/*
struct comp
{
    bool operator()(const node a, const node b)
    {
        return a.r >b.r;
    }
};*/
/*
#define INF (1<<20)
#define pii pair< int, int >
#define pb(x) push_back(x)
#define MAX 100001
struct comp {
    bool operator() (const pii &a, const pii &b) {
        return a.second > b.second;
    }
};*/

/*
ll poww(ll a, ll b)
{

  ll x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
           // if(x>MOD) x%=MOD;
        }
        y = (y*y);
        //if(y>MOD) y%=MOD;
        b /= 2;
    }
    return x;
}
*/
/*
bool prime[1000010];

void primer()
{
    memset(prime,1,sizeof(prime));
   prime[1]=0;

   for(i=2;i*i<=1000000;i++)
   {
     //cout<<i;
      if(prime[i])
      {
         for(j=i*i;j<=1000000;j+=i)
         {
            prime[j]=0;
            //cout<<"j"<<j;
         }
      }
   }

}*/
void mark_digit(lll a[11],lll num)
{
    lll div,rem;
    while(num)
    {
        div=num/10;
        rem=num%10;
        a[rem]=1;
        num=div;
    }
}
bool check(lll a[11])
{
    lll i;
    fr(i,10)
    {
        if(a[i]==0)
            return 0;
    }
    return 1;
}
int main()
{
   lll t,tc;
   slll(t);
   fra(tc,1,t+1)
   {

   lll n,i,ans,num,k;
   //s(n);
   slll(n);
   if(n==0)
   {
     printf("Case #%lld: INSOMNIA\n",tc);
     continue;
   }
     lll a[11];
   memset(a,0,sizeof(a));

   i=1;

   while(1)
   {
       num=n*i;
       mark_digit(a,num);

       if(check(a))
       {
          break;
       }
       i++;
   }
   //if(k==9)
   printf("Case #%lld: %lld\n",tc,num);
   }
}
