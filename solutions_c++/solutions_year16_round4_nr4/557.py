#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

vector<int> know, perm;
int n;

bool debug = false;
int dfs(int m, int done, int t) {
    if (m == n) return true;
    int c = know[perm[m]] | ( ( t >> (perm[m] * n) ) & ((1<<n)-1) );
    if (debug) cerr << perm[m] << " " << bitset<3>(c) << " " << t << endl;
    bool good = true, found = false;
    for (int i = 0; i < n; i++) {
        if ( !(done & (1<<i)) && (c & (1<<i)) ) {
            good = good && dfs(m+1, done | (1<<i), t);
            found = true;
        }
        if (!good) break;
    }
    return good && found;
}

int main() {
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cin >> n;
        know.clear();
        for (int i = 0; i < n; i++) {
            know.push_back(0);
            for (int j = 0; j < n; j++) {
                char c;  cin >> c;
                if (c == '1') know[i] |= (1<<j);
            }
        }
        
        int ans = 1000;
        for (int bs = 0; bs < (1<<(n*n)); bs++) {
            bool good = true;
            perm.clear();
            for (int j = 0; j < n; j++) {
                perm.push_back(j);
            }
            
            do {
                if (!dfs(0, 0, bs)) {
                    good = false;
                    break;
                } 
            } while (next_permutation(perm.begin(), perm.end()));
            
            /*
            if (bs == 0b100000011) {
                cerr << good << endl;
                for (int j = 0; j < perm.size(); j++) cerr << perm[j] << " ";
                cerr << endl;
                
                debug = true;
                cerr << dfs(0, 0, bs) << endl;
                debug = false;
            }*/
            if (good) {
                ans = min(ans, __builtin_popcount(bs));
                /*
                if (ca == 5 && __builtin_popcount(bs) == 2) {
                    cerr << ans << " " << bitset<9>(bs) << endl;
                    debug = true;
                    perm[0] = 2;
                    perm[1] = 1;
                    perm[2] = 0;
                    cerr << dfs(0, 0, bs) << endl;
                }
                debug = false;
                */
                
            }
        }
        cout << "Case #" << ca << ": " << ans << endl;
    }
    return 0;
}