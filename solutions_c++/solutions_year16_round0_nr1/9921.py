#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define pb push_back
#define fst first
#define snd second
#define mkp make_pair
typedef long long ll;
typedef pair<ll,ll> pll;

bool arr[10];

int main() {
//freopen("A-small-attempt0.in", "r", stdin);
    ll n,t;
    
    cin>>t;
    
    for(ll ti=1; ti<=t; ti++){
        cin>>n;
        cout<<"Case #"<<ti<<": ";
        if(n==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        ll now=0;
        ll count=0;
        while(count<10){
            now += n;
            ll now2=now;
            while(now2>0){
                if(!arr[now2%10]) count++;
                arr[now2%10] = true;
                now2 /= 10;
            }
        }
        cout<<now<<endl;
        zero(arr);
    }
    
    return 0;
}
