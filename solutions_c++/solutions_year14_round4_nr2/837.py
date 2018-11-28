#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int T, x, n, s[1007], lbi[1007], rbi[1007], lbn[1007], rbn[1007];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        cin >> n;
        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> s[i];
        }
        /*
        lbi[1] = 0;
        for (int i = 2; i <= n; ++i) {
            lbi[i] = i - 1;
            while (lbi[i] && s[lbi[i]] < s[i]) {
                lbi[i] = lbi[lbi[i]];
            }
        }
        rbi[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            rbi[i] = i + 1;
            while (rbi[i] && s[rbi[i]] < s[i]) {
                rbi[i] = rbi[rbi[i]];
            }
        }
        lbn[1] = 0;
        for (int i = 2; i <= n; ++i) {
            if (lbi[i] == 0)
                lbn[i] = 0;
            else
                lbn[i] = lbn[lbi[i]] + 1;
        }
        rbn[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (rbi[i] == 0)
                rbn[i] = 0;
            else
                rbn[i] = rbn[rbi[i]] + 1;
        }
        */
        memset(lbn, 0, sizeof lbn);
        memset(rbn, 0, sizeof rbn);
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j < i; ++j)
                if (s[j] > s[i]) ++lbn[i];
        }
        for (int i = n; i >= 0; --i) {
            for (int j = n; j > i; --j)
                if (s[j] > s[i]) ++rbn[i];
        }
        /*
        for (int i = 1; i <= n; ++i)
             cout << lbi[i] << '\t' ;
             cout << endl;
        for (int i = 1; i <= n; ++i)
             cout << rbi[i] << '\t' ;
             cout << endl;
        for (int i = 1; i <= n; ++i)
             cout << lbn[i] << '\t' ;
             cout << endl;
        for (int i = 1; i <= n; ++i)
             cout << rbn[i] << '\t' ;
             cout << endl;
        */
        
        for (int i = 1; i <= n; ++i) {
            ans += min(lbn[i], rbn[i]);
        }
        
        printf("Case #%d: %d\n", cs, ans);
        
    }
    return 0;
}
