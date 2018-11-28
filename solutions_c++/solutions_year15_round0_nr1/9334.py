
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

int solve(int n, string &a) {
    int s = 0;
    int f = 0;
    for (int i = 0; i <= n; ++i) {
        if (i > s) {
            f += i - s;
            s = i;
        }
        s += a[i] - '0';
    }
    return f;
}

int main() {
    int t;
    cin >> t;
    fr(u,t) {
        int n;
        cin >> n;
        string a;
        cin >> a;
        cout << "Case #" << u + 1 << ": " << solve(n, a) << "\n";
    }

    return 0;
}
