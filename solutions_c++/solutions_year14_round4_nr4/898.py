#include <iostream>
#include <vector>

#include <set>
#define F first
#define S second
using namespace std;
typedef long long ll;
ll ha = 321312311ll;
ll MOD = 4216321321321421ll;

vector<string> servers[100];
    vector<string> v;
int n;
pair<int, int> best;
int f(int d) {
    if(d < 0) {
        int tot = 0;
        for(int i = 0; i < n; ++i) {
            if(servers[i].size() == 0) return 0;
            set<ll> lol;
            for(int j = 0; j < servers[i].size(); ++j) {
                ll hash = 0;
                for(int k = 0; k < servers[i][j].size(); ++k) {
                    hash = hash * ha + servers[i][j][k];
                    hash %= MOD;
                    hash += MOD;
                    hash %= MOD;
                    lol.insert(hash);
                }
            }
            tot += lol.size() + 1;
        }
        if(tot > best.F) {
            best.S = 1;
            best.F = tot;
        }
        else if(tot == best.F) {
            ++best.S;
        }
        /*
        cout<<"taas... "<<best.F<<'\n';
        for(int i = 0; i < n; ++i) {
            cout<<"IIII "<<i<<' ';
            for(int j = 0; j < servers[i].size(); ++j) {
                cout<<servers[i][j]<<' ';
            }
            cout<<'\n';
        }
        */
        return 0;
    }
    for(int i = 0; i < n; ++i) {
        servers[i].push_back(v[d]);
        f(d-1);
        servers[i].pop_back();
    }
    return 0;
}
int main() {
    int t;
    cin>>t;
    for(int tt = 1; tt <= t; ++tt) {
        cout<<"Case #"<<tt<<": ";
        int m;
        cin>>m>>n;
        v.resize(m);
        for(int i = 0; i < m; ++i) { 
            cin>>v[i];
        }
        best.F = 0;
        best.S = 0;
        f(m-1);
        cout<<best.F<<' '<<best.S<<'\n';


    }
}
