
#include <bits/stdc++.h>
using namespace std;
#define ll long long
/// Set your CPU's L1 data cache size (in bytes) here
const int L1D_CACHE_SIZE = 32768;
int64_t limit = 4294967296;

int64_t low;
map<ll,int> map_prime;
map<ll,ll> map_divide;
vector<ll> v;

ll prime_check(ll n)
{
  for(ll i=2;i*i<=n;i++)
  {
    if(n%i==0)
    {
      map_prime[n]=-1;
      map_divide[n]=i;
      return 1;
    }
  }
  map_prime[n]=1;
  return 0;
}

ll base2(ll n)
{
  ll tmp=0;
  ll a[40]={0};
  ll i=0;
   while(n)
   {
     a[i++]=n%2;
     n/=2;
   }
   for(ll j=i-1;j>=0;j--)
   {
     tmp=tmp*10+a[j];
   }
   return tmp;
}
ll basecheck(ll n,ll b)
{
  ll tmp=0;
  ll a[40]={0};
  ll i=0;
  while(n)
  {
    tmp+=pow(b,i)*(n%10);
    n/=10;
    i++;
  }

   v.push_back(tmp);
    //printf("%lld ",tmp);
   if(map_prime[tmp]==1)
   {
     return 1;
   }
   else if(map_prime[tmp]==0)
   {
      ll res=prime_check(tmp);
      if(res)
      {
        map_prime[tmp]=1;
        return 1;
      }
      else
      return 0;
   }
   else
    return 0;
}
ll divisors(ll n)
{
  //cout <<"hi "<<n <<endl;

  for(ll i=2;i*i<=n;i++)
    if(n%i==0)
      return i;
}
int main()
{
  ll i,j,k,t,m,n,ii;
  scanf("%lld",&t);
  for(ii=0;ii<t;ii++)
  {
    scanf("%lld%lld",&n,&j);
    printf("Case #%lld:\n",ii+1);
    ll cnt=0;
    for(i=pow(2,n-1)+1;i<pow(2,n);i+=2)
    {
      ll tmp=base2(i);
      ll f=1;
      for(k=2;k<=10;k++)
      {
        //printf("%lld ",basecheck(tmp,k));
        if(basecheck(tmp,k)==0)
          f=0;
      }
      //printf("\n");
      //f=0;
      if(f)
      {
         printf("%lld ",tmp);
         for(k=0;k<9;k++)
         {
           if(map_divide[v[k]]!=0)
            printf("%lld ",map_divide[v[k]]);
           else
           printf("%lld ",divisors(v[k]));
         }
         printf("\n");
         cnt++;
      }
      if(cnt==j)
        break;
      v.clear();

    }
  }
  return 0;
}
