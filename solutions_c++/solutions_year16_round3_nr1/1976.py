#include<iostream>
#include<vector>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include <deque>
#include<map>
#include<string>
#include <sstream>
#include<queue>
#include<set>
using namespace std;
#define f(i,a,b) for(ll i=a;i<b;i++)
#define fr(i,a,b) for(ll i=a;i>=b;i--)
#define ff(i,a,b,c) for(int i=a;i<b;i+=c)
#define w(n) while(n>0)
#define vi vector<int>
#define vll vector<long long int>
typedef pair<int,int> PII;
typedef pair<long long int,long long int> PI;
typedef pair<long long int, pair<int,int> > Pli;
typedef pair<int,string> PS;
typedef long long int ll;
typedef int I;
typedef string S;
ll mod_pow(ll a,ll n,ll b){ll res = 1;while(n){if(n&1) {res = (res*a)%b;}a = (a*a)%b;n >>= 1;}return res%b;}
ll mod_div(ll a,ll b,ll md){ll ans = (a*mod_pow(b,md-2,md))%md; return ans;}
ll mul(ll a,ll b,ll md){ return (ll)(a*b)%md;}
ll gcd(ll n,ll m){if(m<=n && n%m==0)return m;if(n<m)return gcd(m,n);else return gcd(m,n%m);}
ll add(ll a,ll b,ll md){a=((a%md)+(b%md))%md;return a;}
ll sub(ll a,ll b,ll md){return add(a,md-b,md);}
ll bC(int n,int r){ll ans=1;if(r>n-r)r=n-r;f(i,1,r+1)ans=(ans*(n-i+1))/(i);return ans;}
I ti=1;
void solve(priority_queue<PII> p,I n)
{
    S ans="";
    if(n%2!=0)
    {
        PII temp=p.top();
        p.pop();
        if(temp.first==1)ans+=(char)(97+temp.second);
        else
        {
            ans+=(char)(97+temp.second);
            temp.first--;
            p.push(temp);
        }
    }
    ans+=" ";
    while(!p.empty())
    {
        PII f=p.top();
        p.pop();
        PII s=p.top();
        p.pop();
        ans+=(char)(f.second+97);
        ans+=(char)(s.second+97);
        if(f.first>1){f.first--;p.push(f);}
        if(s.first>1){s.first--;p.push(s);}
        ans+=" ";
    }
    cout<<"Case #"<<ti<<": "<<ans<<endl;
    ti++;
}
I main()
{
    I t;
    cin>>t;
    w(t)
    {
        t--;
	    I n;
        cin>>n;
        priority_queue<PII> p;
        I val=0;
        f(i,0,n)
        {
            I x;
            cin>>x;
            val+=x;
            p.push(make_pair(x,i));
        }
        solve(p,val);
    }
}
