#include<bits/stdc++.h>
#define null NULL
#define pb push_back
#define vll vector<long long>
#define vd vector<double>
#define vc vector<char>
#define vv vector<vector <long long>>
#define w(t) while(t--)
#define pqll priority_queue<ll>
#define ll long long
#define sll(a) scanf("%lld",&a)
#define sc(a) scanf("%c",&a)
using namespace std;
ll dp[1000001];
ll dig(ll n)
{
    ll c=0;
    while(n)
    {
        c++;
        n/=10;
    }
    return c;
}
ll rev(ll n)
{
    ll r=0;
    while(n>0)
    {
        r=(r*10)+(n%10);
        n/=10;
    }
    return r;
}
ll compute(ll n)
{
    if(n==1)
    {
        dp[n]=1;
        return 1;
    }
    if(dp[n]!=-1)
        return dp[n];
    ll r=rev(n);
    if(r<n && dig(r)==dig(n))
    {
        dp[n]= 1+min(compute(rev(n)),compute(n-1));
        if(n==10)
        {
            //cout<<r<<dig(r)<<" "<<dig(n)<<" in"<<endl;
        }
    }
    else
        dp[n]=1+compute(n-1);
    return dp[n];
}


int main()
{
    ll t;
    cin>>t;
    ll x=1;
    for(int i=0;i<1000001;i++)
        dp[i]=-1;
    for(int i=1;i<=1000000;i++)
        compute(i);
    for(ll i=1;i<=t;i++)
    {
        ll n;

        sll(n);
        cout<<"Case #"<<i<<": "<<dp[n]<<endl;

    }


    return 0;
}
