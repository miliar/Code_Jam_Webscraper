#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

int pop_count(int x) {
    int ans = 0;
    while (x) {
        ++ans;
        x &= x - 1;
    }
    return ans;
}                     

bool CAN(int msk, int x, int y, int n) {
    return (msk >> (n * (n - x - 1) + n - y - 1)) & 1;
}


bool ok(int x, int n, int target, int msk, int busy) {
    if (x == n) {
        return (busy == 0);
    }
    if (x == target) {
        return ok(x + 1, n, target, msk, busy);
    }
    for (int to = 0; to < n; ++to) {
        if ((busy & (1 << (n - to - 1))) == 0) {
            continue;
        }
        if (CAN(msk, x, to, n) && ok(x + 1, n, target, msk, busy ^ (1 << (n - to - 1)))) {
            return true;
        }
    }
    return ok(x + 1, n, target, msk, busy);
}


int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {        
        int n;
        cin >> n;


        int msk = 0;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < n; ++j)
                msk = (msk << 1) + (s[j] == '1');
        }

        int ans = n * n;
        for (int m = 0; m < (1 << (n * n)); ++m) {
            if ((m & msk) != msk) {
                continue;
            }
            int ed = pop_count(m ^ msk);
            if (ed >= ans) {
                continue;
            }

            bool fail = false;
            for (int i = 0; i < n; ++i) {
                int busy = ((m >> (n * (n - i - 1))) & ((1 << n) - 1));
                if (ok(0, n, i, m, busy)) {
                    fail = true;
                    break;
                }
            }
            if (fail) {
                continue;
            }

            ans = ed;
            /*
            cerr << m << endl;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j)
                    cerr << CAN(m, i, j, n);
                cerr << endl;
            }
            cerr << endl;               
            */
        }

        cout << "Case #" << test << ": ";
        cout << ans;
        cout << endl;
    }

    return 0;
}
