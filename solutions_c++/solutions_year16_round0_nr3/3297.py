#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
const ll MN = 1ll<<20;
vector<ll> ddd;
int main() {
    ddd.resize(MN);
    for(ll i = 2; i*i <= MN; ++i) {
        if(ddd[i] == 0) {
            for(ll j = i*i; j <= MN; j += i) {
                ddd[j] = i;
            }
        }
    }
    ll tt;
    ll nn,jj;
    cin>>tt;
    cin>>nn>>jj;

    for(ll xx = 0; xx < tt; ++xx) {
        cout<<"Case #"<<xx+1<<":\n";
        ll lol = 0;
        for(ll i = 1; i < (1ll<<(nn-1)); i += 2) {
            ll q = i|(1ll<<(nn-1));
            vector<ll> ans;
//            cout<<i<<'\n';
            for(ll j = 2; j <= 10; ++j) {
                __int128_t res = 0;
                ll z = q;
                __int128_t lol = 1;
                for(ll k = 0; k < nn; ++k) {
                    if(z&1) res += lol;
                    z /= 2;
                    lol *= j;
                }
                if(1) {
                    for(ll k = 2; k*k <= res && k < 10000; ++k) {
                        if(res % k == 0) {
                            ans.push_back(k);
                            break;
                        }
                    }
                }
                else {
                    if(ddd[res]) ans.push_back(res);//;ddd[res]);
                }
            }
            vector<ll> v;
            if(ans.size() == 9) {
                ++lol;
                ll z = q;
                for(ll k = 0; k < nn; ++k) {
                    v.push_back(z&1);
                    z /= 2;
                }
                for(ll j = 0; j < v.size(); ++j) {
                    cout<<v[v.size()-j-1];
                }
                cout<<' ';
                for(auto x: ans) cout<<x<<' ';
                cout<<'\n';
                if(lol == jj) {
                    return 0;
                }
            }
        }
    }
}
