#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string s;
ll n, m, num, ans;

ll mult(ll a, ll b) {
    int sign = 1;
    if (a * b < 0) sign = -1;
    a = abs(a);
    b = abs(b);
    if (b == 1) return a * sign;
    if (a == 1) return b * sign;
    if (a == b) return -sign;
    if (a == 2 && b == 3) return 4 * sign;
    if (a == 2 && b == 4) return -3 * sign;
    if (a == 3 && b == 2) return -4 * sign;
    if (a == 3 && b == 4) return 2 * sign;
    if (a == 4 && b == 2) return 3 * sign;
    if (a == 4 && b == 3) return -2 *sign;
}

ll pot(ll a, ll p) {
    if (p == 1) return a;
    if (p % 2 == 1) {
        return mult(a, pot(a, p-1));
    } else {
        return mult(pot(a, p/2), pot(a, p/2));
    }
}

int main() {
    int t;
    cin >> t;
    for (int z = 1; z <= t; z++) {
        cin >> n >> m >> s;
        num = 1;
        for (int i = 0; i < (int)s.size(); i++) {
            num = mult(num, s[i] - 'i' + 2);
        }
        ans = pot(num, m);
        if (ans != -1) {
            printf("Case #%d: NO\n", z);
            continue;
        }
        string r = s;
        int limit;
        if (m > 8) limit = 8;
        else limit = m;
        for (int i = 1; i < limit; i++) s += r;
        if (m <= 8) {
            s.erase(s.begin() + (int)s.size() - 1);
        }
        int cond = 0;
        num = 1;
        for (int i = 0; i < (int)s.size(); i++) {
            num = mult(num, s[i] - 'i' + 2);
            if (cond == 0 && num == 2) cond = 1;
            if (cond == 1 && num == 4) cond = 2;
        }
        if (cond == 2) {
            printf("Case #%d: YES\n", z);
        } else {
            printf("Case #%d: NO\n", z);
        }
    }
    return 0;
}
