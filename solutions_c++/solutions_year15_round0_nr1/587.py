#include <bits/stdc++.h>

#define mp make_pair
#define fs first
#define sc second
#define pb push_back
#define eb emplace_back

#define y0 yy0
#define y1 yy1
#define next _next
#define prev _prev
#define link _link
#define hash _hash

#define sz(s) int((s).size())
#define len(s) int((s).size())
#define all(s) (s).begin(), (s).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ll lINF = 1e18;
const double EPS = 1e-12;

using namespace std;

int n, t;

string s;

int main()
{
#ifdef DEBUG
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
#endif

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        cin >> s;
        int ans = 0;
        for (int j = 0, sum = 0; j < len(s); j++) {
            ans = max(ans, j - sum);
            sum += s[j] - '0';
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}
