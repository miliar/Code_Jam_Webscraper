
/*
 * “Doktor! Are you sure this will work?!”
 * “Ha-ha! I have NO IDEA!”
 */

/*
 * short     2^15-1 ~ 3e4
 * int       2^31-1 ~ 2e9
 * long x86  2^31-1 ~ 2e9
 * long long 2^63-1 ~ 9e18
 */

#include <bits/stdc++.h>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define fr(a,b) for (int a=0; a<b; ++a)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const ll mod = 1000000007ll;
const int infty = numeric_limits<int>::max();
struct _{_(){ios_base::Init i;ios_base::sync_with_stdio(0);cin.tie(0);}}_;

ull solve(int n) {
    ull a = n;
    bool b[10] = {};
    bool ok;
    while (true) {
        // cerr << a << endl;
        for (ull t = a; t > 0; t /= 10) {
            b[t%10] = true;
            // cerr << "---" << t%10 << endl;
        }
        ok = true;
        fr(i, 10) {
            if (!b[i]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return a;
        } else {
            a += n;
        }
    }
}

int main() {
    int t;
    cin >> t;
    fr(u,t) {
        int n;
        cin >> n;
        if (!n) {
            cout << "Case #" << u+1 << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << u+1 << ": " << solve(n) << endl;
        }
    }

    return 0;
}
