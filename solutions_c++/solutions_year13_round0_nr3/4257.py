#include<cstdio>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<stack>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<utility>
#define f0(i,a) for(__typeof(a)i=0;i<a;i++)
#define f1(i,a) for(__typeof(a)i=1;i<=a;i++)
#define fa0(i,a) for(__typeof(a)i=a;i>=0;i--)
#define FORab(i,a,b) for(__typeof(a)i=a;i<=b;i++)
#define pf printf
#define sf scanf
#define si(a) scanf("%d",&a)
#define sd(a) scanf("%lf",&a)
#define G getchar()
#define sl strlen
#define nl printf("\n")
#define memo(str,a) memset(str,a,sizeof(str))
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
#define ll long long
#define pb push_back
#define srt(arr,n) sort(arr,arr+n)
#define rev(arr,n) reverse(arr,arr+n)
#define pi acos(-1.0)
#define popc __builtin_popcount
#define gcd __gcd
#define pii pair<int ,int >
#define all(a) a.begin(),a.end()
using namespace std;
#define MAX 100000000000002
vector<int>v,vt,pals;
bool check(ll num)
{
    v.clear();
    while(num>0)
    {
        v.pb(num%10);
        num/=10;
    }
    vt=v;
    reverse(all(vt));
    if(v==vt) return true;
    return false;
}
void palcreate()
{
    pals.clear();
    ll i;
    for(i=1;i*i<=MAX;i++)
    {
        if(check(i) && check(i*i)) pals.pb(i*i);
    }
}
int main()
{
	//freopen("d:\\input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
    palcreate();
    ll x=pals.size();
    ll t,a,b,idx,ans;
    cin>>t;
    f1(cs,t)
    {
        cin>>a>>b;
        ans=0;
        for(idx=0;pals[idx]<a,idx<x;idx++){}
        for(idx;idx<x,pals[idx]<=b;idx++,ans++){}
        pf("Case #%lld: %lld\n",cs,ans);
    }
	return 0;
}
