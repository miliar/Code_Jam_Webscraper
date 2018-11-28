#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll a[10];
ll c=0;
void check(ll k)
{
    while(k>0)
    {
      if(a[k%10]==0)
      c++;
      a[k%10]++;
      k=k/10;
    }
}
int main()
{
    ll t,n,i,ans;
    ios::sync_with_stdio(false);
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    ll r=1;
    while(r<=t)
    {
        cin>>n;
        ans=0;
        memset(a,0,sizeof(a));
        c=0;
        if(n==0)
        {
         cout<<"Case #"<<r<<": INSOMNIA"<<endl;
         r++;
        }
        else
        {
        check(n);
        ll num=1;
        while(c<10)
        {
         num++;
         ans=num*n;
         check(ans);
        }
        cout<<"Case #"<<r<<": "<<ans<<endl;
          r++;
        }


    }
}
