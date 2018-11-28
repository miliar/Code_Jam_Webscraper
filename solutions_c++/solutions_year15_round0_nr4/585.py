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

#ifdef WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ll lINF = 1e18;
const double EPS = 1e-12;

using namespace std;

int ttt;

int main()
{
#ifdef DEBUG
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
#endif

    scanf("%d", &ttt);

    for (int tt = 1; tt <= ttt; tt++) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        if (r < c) {
            swap(r, c);
        }
        printf("Case #%d: ", tt);
        if (x == 1) {
            printf("GABRIEL\n");
        } else if (x == 2) {
            if ((r * c) % 2 == 0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if (x == 3) {
            if (r >= 3 && c >= 2 && (r * c) % 3 == 0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if (x == 4) {
            if (r >= 4 && c >= 3 && (r * c) % 4 == 0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if (x == 5) {
            if (r >= 5 && c >= 3 && (r * c) % 5 == 0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if (x > 5) {
            printf("RICHARD\n");
        }
    }
    return 0;
}
