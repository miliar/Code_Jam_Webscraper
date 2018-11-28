// * Temmiy accidentally misspells her own name.
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
using namespace std;
#define rep(i,a,n) for (int i=a;i<(n);i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef long long ll;

void solve() {
    int n;
    cin >> n;
    bool m0[n][n];
    rep(i, 0, n) {
        string s;
        cin >> s;
        rep(j, 0, n) m0[i][j] = s[j] == '1';
    }
    int best = 100000;
    rep(mask, 0, 1 << (n * n)) {
        bool m[n][n];
        int cost = __builtin_popcount(mask);
        rep(i, 0, n)rep(j, 0, n) {
            m[i][j] = m0[i][j] || (mask & (1 << (i * n + j)));
        }
        //rep(i,0,n){rep(j,0,n)cout<<m[i][j];cout<<endl;}
        bool good = true;
        rep(i, 0, n) {
            bool k = false;
            rep(j, 0, n) if(m[j][i]) k = true;
            if(!k) good = false;
        }
        if(!good) continue;
        rep(cur, 0, n) {
            vector<int> ord;
            rep(i,0,n) ord.push_back(i);
            do {
                vector<bool> done(n, false);
                rep(i,0,n){
                    if(i==cur) continue;
                    if(m[i][ord[i]]){
                        done[ord[i]] = true;
                    }
                }
                bool k = false;
                rep(i,0,n) if(m[cur][i] && (!done[i])){
                    k = true;
                }
                if(!k){
                    good = false;
                    break;
                }
            } while(next_permutation(ord.begin(), ord.end()));
        }
        if(!good) continue;
        //rep(i,0,n){rep(j,0,n)cout<<m[i][j];cout<<endl;}cout<<endl;
        best = min(best, cost);
    }
    cout<<best;
}

int main() {
    freopen("small.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
