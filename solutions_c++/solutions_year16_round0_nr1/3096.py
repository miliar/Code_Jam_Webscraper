/*input
10
21
22
23
24
25
26
27
28
29
30
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 1000000009
#define mod 1000000007
vector <ll> v,v1,ans;
ll mark[20];
int main() 
{
    std::ios::sync_with_stdio(false);
    ll t,tc;
    cin>>t;
    tc=0;
    while(t--)
    {
        tc++;
        cout<<"Case #"<<tc<<": ";
        v.clear();
        v1.clear();
        ans.clear();
        memset(mark,0,sizeof(mark));
        ll n;
        cin>>n;
        if(n>0)
        {
            ll temp = n;
            while(temp>0)
            {
                ll d = temp%10;
                v.push_back(d);
                //mark[d]=1;
                temp = temp/10;
            }
            ll mul = 1;
            bool f = 0;
            while(!f)
            {
                bool f1=0;
                F(i,0,9)
                {
                    if(!mark[i])
                    {
                        f1 = 1;
                        break;
                    }
                }
                if(!f1)
                {
                    f = 1;
                    break;
                }
                ll sum=0,carry=0;
                ll sz = v.size();
                F(i,0,sz-1)
                {
                    sum = carry + v[i]*mul;
                    carry = sum/10;
                    sum = sum%10;
                    v1.push_back(sum);
                }
                while(carry>0)
                {
                    sum = carry%10;
                    carry = carry/10;
                    v1.push_back(sum);
                }
                sz = v1.size();
                ans = v1;
                RF(i,sz-1,0)
                {
                    //cout<<v1[i];
                    mark[v1[i]]=1;
                }
                v1.clear();
                //cout<<endl;
                mul++;
            }
            ll sz = ans.size();
            RF(i,sz-1,0)
                cout<<ans[i];
            cout<<endl;
        }
        else
        {
            cout<<"INSOMNIA"<<endl;
        }
    }    
    return 0;
}