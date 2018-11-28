#include "bits/stdc++.h"

using namespace std;

#define sz(a) int((a).size())
#define all(x) x.begin(), x.end()
#define pb push_back
#define F first
#define S second
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
const int inf = 1e9 + 7;
const ld eps = 1e-8;




int main() {
#ifdef DEBUG
    //freopen("/Users/rzmn/Documents/acm/acm/input.txt", "r", stdin);
    //freopen("/Users/rzmn/Documents/acm/acm/output.txt", "w", stdout);
#endif
    
    
    
    int Tcase; scanf("%d", &Tcase);
    for (int test = 1; test <= Tcase; ++test) {
        string s; cin >> s;
        int iter = 0, r = sz(s) - 1;
        for (;;) {
            while (r >= 0 && s[r] == '+') --r;
            if (r == -1) break;
            int l = r;
            while (l >= 0 && s[l] == '-') --l;
            if (l == -1) { for (int it = 0; it <= r; ++it) s[it] = '+'; ++iter; }
            else {
                l = 0;
                while (s[l] == s[0]) ++l;
                l -= (s[l] != s[0]);
                if (s[0] == '-') {
                    for (int it = 0; it <= r; ++it)
                        s[it] = (s[it] == '+' ? '-' : '+');
                    ++iter;
                }
                else {
                    for (int it = 0; it <= l; ++it)
                        s[it] = '-';
                    ++iter;
                    for (int it = 0; it <= r; ++it)
                        s[it] = (s[it] == '+' ? '-' : '+');
                    ++iter;
                }
            }
        }
        printf("Case #%d: %d\n", test, iter);
    }
    
    
    
    
#ifdef DEBUG
    cerr << "\n == TIME : " << clock() / ld(CLOCKS_PER_SEC) << " == " << endl;
#endif
}

// 14 27













