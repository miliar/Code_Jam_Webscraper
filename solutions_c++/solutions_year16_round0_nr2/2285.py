
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

int solve(const string &s) {
    int c = 0;
    int n = (int)s.length();
    for (int i = 1; i < n; ++i) {
        if (s[i-1] != s[i]) {
            ++c;
        }
    }
    if (s[n-1] == '-') {
        ++c;
    }
    return c;
}

int main() {
    int t;
    cin >> t;
    fr(u,t) {
        string s;
        cin >> s;
        cout << "Case #" << u+1 << ": " << solve(s) << endl;
    }

    return 0;
}
