#include<bits/stdc++.h>
using namespace std;
typedef  long long ll;
ll mod;
inline ll multiply(ll a,ll b)   // O(1) for (a*b)%m
{
   a %= mod;
   b %= mod;
   long double res = a;
   res *= b;
   ll c = ll(res / mod);
   a *= b;
   a -= c * mod;
   a %= mod;
   if (a < 0) a += mod;
   return a;
}

inline ll power(ll a,ll b)
{
   ll ans=1;
   while(b)
   {
           if(b&1)
           {
                     ans=multiply(ans,a);
           }
           a=multiply(a,a);
           b>>=1;
   }
   return ans;
}
int b[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
inline bool Miller(ll p)
{
    if(p<2)  return false;
    if(p!=2 && !(p&1)) return false;
    for(int i=0;i<25;i++)
    {
            if(p==b[i])return true;
            else if(p%b[i]==0)return false;
    }
    int count = 0;
    long long s=p-1;
    while(!(s&1))
    {
        s/=2;
        count++;
    }
    ll accuracy=10;
    for(int i=0;i<accuracy;i++)
    {
        long long a=rand()%(p-1)+1;
        mod=p;
        long long x=power(a,s);
        if(x == 1 || x == p-1) continue;
        int flag = 0;
        for(int i = 1; i < count; i++)
        {
           x = multiply(x,x);
           if(x == 1) return false;
           if(x == p-1)
           {
              flag = 1;
              break;
           }
        }
        if(flag) continue;
        return false;
    }
    return true;
}
ll n,J;
ll func(ll i,ll val)
{
    if(J==0)
    return 0;
    if(i==n)
    {
        if(val%10==0)
        return 0;
        else
        {
            ll p=val;
            ll count1=0;
            ll a[15];
            memset(a,0,sizeof(a));
            while(p!=0)
            {
                ll r=p%10;
                for(ll base=2;base<=10;base++)
                {
                    a[base]+=r*pow(base,count1);
                }
                p=p/10;
                count1++;
            }
            int flag=1;
            for(ll base=2;base<=10;base++)
            {
                if(Miller(a[base])==1)
                {
                    flag=0;
                    return 0;
                    break;
                }


            }
            if(flag==1)
            {
                printf("%lld ",val);
                ll j;
                for(ll base=2;base<=10;base++)
                {
                    for( j=2;j<=sqrt(a[base]);j++)
                    {
                        if(a[base]%j==0)
                        break;
                    }
                    printf("%lld ",j);
                }
                printf("\n");
                J--;
            }
        }
    }
    else
    {
        func(i+1,val*10+0);
        func(i+1,val*10+1);
    }
}
int main()
{
   // prime1();
    ll t,p,i,j,r,c=1,l,k;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld%lld",&n,&J);
        printf("Case #%lld:\n",c++);
        func(1,1);
        //printf("%lld\n",ans);
    }
    return 0;
}
