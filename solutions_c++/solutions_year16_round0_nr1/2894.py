#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef pair<ll,ll> PLL;

int main(void) {
    int n;
    cin>>n;
    FOR(i,0,n) {
        ll x,ans=-1;
        cin>>x;
        set<int> s;
        if(x==0) { s.insert(0); }
        FOR (k,0,100) {
            ll y = x * (1+k);
            while(y>0) {
                s.insert(y%10);
                y /= 10;
            }
            if(s.size()==10) {
                ans= x * (1+k);
                break;
            }
        }
        if(ans==-1) cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
        else        cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
    }
}
