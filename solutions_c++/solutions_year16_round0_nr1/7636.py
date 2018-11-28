#include<bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define M 1000000009
#define REM 4
#define N 100005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define f(i,n) for(i=0;i<n;i++)
#define foi(i,j,k) for(i=j;i<k;i++)
#define mll map<ll,ll>
#define foe(i,j,k) for(i=j;i<=k;i++)
 
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;



int main()
{
    ll n,k,q,i,j,p,cnt,ans;
    ll t;
    sl(t);
    i=0;
    while(i<t)
    {
      
      
      sl(n);
      cnt=0;
      ans=n;
      if(n==0)
       cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
      else
      {
      	bool arr[10]={0};
        k=n;p=1;cnt=0;
        while(cnt<10)
        {
           k=n*p;
           ans=k;
        while(k>0)
        {
          if(arr[k%10]==0)
          {  arr[k%10]=1;cnt++;}
            k=k/10;  
           if(cnt==10)break;
        }
         p++;
          }
           cout<<"Case #"<<i+1<<": "<<ans<<endl;
      }
      i++;
    }


    return 0;
}
