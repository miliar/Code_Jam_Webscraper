#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

ld p[205];
int main() {
    int t; cin >> t;

    for (int ca = 1; ca <= t; ca++) {
        int n, k; cin >> n >> k;
        
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }


        ld ans = 0;
        for (int bs = (1<<k)-1; bs < (1<<n); bs++) {
            if (__builtin_popcount(bs) != k) continue;
            vector<int> id;
            for (int i = 0; i < n; i++) {
                if (bs & (1<<i)) id.push_back(i);
            }
            
            ld prob = 0;
            for (int bs2 = (1<<k/2)-1; bs2 < (1<<id.size()); bs2++) {
                if (__builtin_popcount(bs2) != k/2) continue;
                ld tprob = 1;
                for (int j = 0; j < id.size(); j++) {
                    if ((1<<j) & bs2) tprob *= p[id[j]];
                    else tprob *= (1-p[id[j]]);
                }
                prob += tprob;
            }
            //cerr << bitset<4>(bs) << " " << prob << endl;
            ans = max(prob, ans);
        }
        cout << "Case #" << ca << ": " << fixed << setprecision(8) << ans << endl;
    }
    return 0;
}