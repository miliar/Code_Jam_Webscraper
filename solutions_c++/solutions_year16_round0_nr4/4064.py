#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
#define f(i,a,b) for(int i=a;i<b;i++)
typedef long long int ll;
typedef int I;
ll mod_pow(ll a,ll n,ll b){ll res = 1;while(n){if(n&1) {res = (res*a)%b;}a = (a*a)%b;n >>= 1;}return res%b;}
ll mod_div(ll a,ll b,ll md){ll ans = (a*mod_pow(b,md-2,md))%md; return ans;}
ll mul(ll a,ll b,ll md){ return (ll)(a*b)%md;}
void add(ll &a,ll b,ll md){a=((a%md)+(b%md))%md;}
void sub(ll &a,ll b,ll md){add(a,md-b,md);}
I s[32];
void solve(ll x)
{
    I k=0;
    while(x>0)
    {
        if(x%2==1)s[k]++;
        x/=2;
        k++;
    }
}
void ans()
{
    ll a=0;
    f(i,0,32)
        a+=pow(2,i)*s[i]*(s[i]-1)/2;
    cout<<a<<endl;
}
int main()
{
    int n;
    cin>>n;
    ll a[n];
    f(i,0,32)s[i]=0;
    f(i,0,n)cin>>a[i];
    f(i,0,n)
       solve(a[i]);
    ans();
}

