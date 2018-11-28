#include<bits/stdc++.h>
#define ll long long int
using namespace std;

ll a[20];
vector<ll> v;


ll modpow(ll base, ll exp, ll modulus) {
  base %= modulus;
  ll result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

int div(ll n)
{
    ll i;

    if (n==2)
        return 1;

    if (n%2==0)
        return 2;

    for (i=3;i<=sqrt(n);i+=2)
        if (n%i==0)
            return i;

    return 1;
}

ll power(ll x, ll y)
{
    ll temp;
    if( y == 0)
       return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
    {
        if(y > 0)
            return x*temp*temp;
        else
            return (temp*temp)/x;
    }
}


void SieveOfEratosthenes(int n)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));

    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
    for (int p=2; p<=n; p++)
       if (prime[p])
          v.push_back(p);
}

void ps()
{
    ll pow_set_size = pow(2,14);
    ll counter, j,ans1[20],ans,ansdiv[20],cnt=0;
    for(ll i=2;i<=10;i++)
        ans1[i]=power(i,15);
    for(counter = 0; counter < pow_set_size&&cnt<500; counter++)
     {
      int k=0;
      for(j = 0; j < 14; j++)
       {
          if(counter & (1<<j))
           {
               a[k++]=1;
           }
           else
           {
               a[k++]=0;
           }
       }
       ll pos=0;
       for(int x1=2;x1<=10;x1++)
       {
          ll pos2=1;
          ans=ans1[x1];
          for(int i=0;i<k;i++)
          {
           if(a[i]==1)
            ans+=power(x1,15-i-1);
          }
          ans+=1;
          ll ans11=ans;
          for(int i=0;i<150;i++)
          {
              ans11=((ans%v[i])+modpow(x1,31,v[i]))%v[i];
              if(ans11==0)
              {
                  ansdiv[x1]=v[i];
                  pos2=0;
                  break;
              }
          }
          if(pos2==1)
          {
              pos=1;
              break;
          }
       }
       if(pos==1)
       {
           continue;
       }
       else
       {
           cnt++;
           printf("1");
           for(int i=31;i>16;i--)
            printf("0");
           printf("1");
           for(int i=0;i<k;i++)
            printf("%d",a[i]);
           printf("1");
           printf(" ");
           for(int i=2;i<=10;i++)
            printf("%d ",ansdiv[i]);
           printf("\n");
       }
    }
}

int main()
{
    int t,n,m;
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d%d",&n,&m);
        SieveOfEratosthenes(1000);
       // cout<<(modpow(10,31,191)+modpow(10,15,191)+modpow(10,14,191)+modpow(10,12,191)+modpow(10,11,191)+modpow(10,9,191)+modpow(10,0,191))%191<<endl;
        printf("Case #%d:\n",i);
        ps();
    }
    return 0;
}
