#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define f(i,s,e) for(i=s;i<=e;i++)
#define INF 10000000000
#define PII pair<ll, int>;
#define pb push_back
#define mp make_pair
queue<pair<ll,ll> > q;
stack<pair<ll,ll> > s;
bool flag[20]={0};
int main()
{
    ll t=0,tc;
    //freopen("Alar.in","r",stdin);
    //freopen("Alarop.in","w",stdout);
    scanf("%lld",&tc);while(t<tc)
    {
      t++;
      ll n,cnt=0,i,j,orig;
      scanf("%lld",&orig);
      if(orig==0)
      {
          cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
          continue;
      }
      for(i=0;i<=15;i++) flag[i]=false;
      for(i=1;cnt<10;i++)
      {
          n=orig*i;//cout<<"n "<<n<<endl;
          ll temp=n;
          while(temp>0)
          {
              ll x=temp%10;
              temp=temp/10;
              if( !flag[x] )
              {
                  flag[x]=true;
                  cnt++;//cout<<"cnt : "<<cnt<<endl;
              }
              if(cnt==10)
              {
                  cout<<"Case #"<<t<<": "<<n<<endl;
                  break;
              }
          }
      }
    }
}

