#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll reverse(ll x) {
    ll ans = 0;
    while(x) {
        ll d = x % 10;
        ans = 10LL * ans + d;
        x /= 10;
    }
    return ans;
}

int main() {
    ifstream cin("testA.in");
    ofstream cout("testA.out");

    int t; cin >> t;
    
    vector<ll> pTen(16, 1);
    for(int i = 1; i < 16; ++i)
        pTen[i] = 10LL * pTen[i - 1]; 
    
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        ll x; cin >> x;
        ll start = 1;
        ll ops = 1, digits = 1;
        ll ans = x;

        while(start != x) {
            ll last = start;
            ll nextTen = pTen[digits];
            start = min(nextTen, x);
            ops += start - last;
            digits++;
            ans = min(ans, ops + x - start);
            if(start == x)
                break;
            if(x >= pTen[digits]) {
                start = reverse(start + pTen[digits / 2] - 1);
                ops += pTen[digits / 2] - 1 + 1;
            } else {
                ll minn = x;
                ll sol = -1;
                cerr << x << " " << start << "\n";
                ll revX = 0, lim = pTen[digits / 2] - 1;
                if(x % 10) {
                    revX = reverse(x);
                    sol = revX % pTen[digits / 2];
                } else {
                    for(ll append = lim; append >= 1; --append) {
                        ll value = reverse(start + append);
                        if(value <= x) {
                            if(x - value <= minn) {
                                sol = append;
                                minn = x - value;
                            }
                        }
                    }
                }
                start = reverse(start + sol);
                ops += sol + 1;
            }
            ans = min(ans, ops + x - start);
        }
        
        cout << ans << "\n";
    }
}
