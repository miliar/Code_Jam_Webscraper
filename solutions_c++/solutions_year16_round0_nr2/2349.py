#include <iostream>
#include <string>
#include <queue>
#include <tuple>
#include <bitset>
#include <cassert>
#include <algorithm>

using namespace std;
using ll = long long;
const ll inf = 1e9;
#define rep(i,n) for(int i = 0; i < (int)(n); ++i)

using bits = bitset<16>;
namespace std {
    bool operator < (const bits &a, const bits &b){
        return a.to_ulong() < b.to_ulong();
    }
}

int solve(const string s){
    bits S = 0;
    int n = s.size();
    rep(i,n) S[i] = s[i] == '+';
    int dist[70000];
    fill(dist,dist+70000,inf);
    dist[S.to_ulong()] = 0;
    priority_queue<pair<int,bits>> q;
    q.emplace(0,S);

    while(q.size()){
        int d;
        bits S;
        tie(d,S) = q.top(); q.pop();
        d = -d;
        assert((int)S.to_ulong() <= (1<<n));
        if((int)S.count() == n) return d;

        for(int i = 1; i <= n; ++i){
            int nd = d+1;
            bits nS = S;
            for(int j = 0; j < i; ++j){
                bool a = S[j];
                nS[i-j-1] = !a;
            }
            if(dist[nS.to_ulong()] >= nd){
                dist[nS.to_ulong()] = nd;
                q.emplace(-nd, nS);
            }
        }
    }
    return -1;
}

int solveLarge(string s){
    int n = s.size();
    int ans = 0;
    rep(i,n-1){
        if((s[i] == '-') ^ (s[i+1] == '-')){
            reverse(s.begin(), s.begin()+i+1);
            rep(j,i+1){
                s[j] = "-+"[s[i] == '-'];
            }
            ++ans;
        }
    }
    if(s[0] == '-') ++ans;
    return ans;
}

int main(){
    // for(int w = 1; w <= 10; ++w){
    //     for(int S = 0; S < 1024; ++S){
    //         string s;
    //         rep(i,w){
    //             s += "+-"[S>>i&1];
    //         }
    //         int x = solve(s);
    //         int y = solveLarge(s);
    //         if(x != y){
    //             cout << s << endl;
    //         }
    //     }
    // }
    // return 0;

    int T;
    cin >> T;
    for(int i = 0; i < T; ++i){
        string s;
        cin >> s;
        ll x = solveLarge(s);
        // int y = solve(s);
        // assert(x == y);
        assert(x != -1);
        printf("Case #%d: %lld\n", i+1, x);
    }
}
