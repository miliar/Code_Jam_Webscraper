#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<bits/stdc++.h>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<bitset>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define mod 1000000007
#define mod1 mod
#define mod2 100000009
#define li long long int
#define ll int
#define readi(x) scanf("%d",&x)
#define  reads(x)  scanf("%s", x)
#define readl(x) scanf("%I64d",&x)
#define rep(i,n) for(i=0;i<n;i++)
#define revp(i,n) for(i=(n-1);i>=0;i--)
#define myrep1(i,a,b) for(i=a;i<=b;i++)
#define myrep2(i,a,b) for(i=b;i>=a;i--)
#define pb push_back
#define mp make_pair
#define fi first
#define sec second
#define MAXN 1000000000000000100
#define MINN -10000000000000
#define pii pair<li,li> 
#define pic pair<int,char>
#define N 200010
#define lgn 20
#define ddouble long double
#define minus minu
#define INTMAX 1000
using namespace std;
using namespace __gnu_pbds;
typedef priority_queue<pii, vector<pii> > max_pq;
typedef priority_queue<pii , vector<pii > ,greater<pii > > min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;
int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin>>t;
    for(ll x=1;x<=t;x++)
    {
        ll k;
        string c;
        cin>>c>>k;
        ll ans=0;
        for(ll i=c.size()-1;i>=(k-1);i--)
        {
            if(c[i]=='-')
            {
                ans++;
                for(ll j=(i-k+1);j<=(i);j++)
                {
                    if(c[j]=='+')
                        c[j]='-';
                    else
                        c[j]='+';
                }
            }
        }
        ll cnt=0;
        for(ll i=0;i<c.size();i++)
        {
            if(c[i]=='+')
                cnt++;
        }
        cout<<"Case #"<<x<<": "
;        if(cnt==c.size())
        {
            cout<<ans<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
}

 