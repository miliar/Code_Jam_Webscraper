#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define fr(i,beg,end) for(i=beg;i<end;i++)
#define itfr(it,stl) for(it=stl.begin();it!=stl.end();it++)
#define PII pair<int,int>
#define init(x,val) memset(x,val,sizeof(x))
#define fst first
#define snd second
using namespace std;
ll power(ll a, ll b)
{
    ll res=1;
    while(b>0)
    {
        if(b&1)
            res=res*a;
        a*=a;
        b>>=1;
    }
    return res;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,T;
    ll k,c,s;
    cin>>T;
    fr(t,1,T+1)
    {
        cin>>k>>c>>s;
        ll ans=1;
        ll p=power(k,c-1);
        cout<<"Case #"<<t<<": ";
        while(s--)
        {
            cout<<ans<<" ";
            ans+=p;
        }
        cout<<endl;
    }
    return 0;
}
