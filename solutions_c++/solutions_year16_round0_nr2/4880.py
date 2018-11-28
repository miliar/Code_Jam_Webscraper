#include <bits/stdc++.h>

#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define sz(s) ((int) strlen (s))
#define all(s) s.begin (), s.end ()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

const int N = 109;
const int inf = (int) 2e9;
const ll linf = (ll) 9e18;
const int mod = (int) 1e9 + 7;

int dp[N][2];

char s[N];

int get (int i, int j) {
        int &ret = dp[i][j];
        if (i == 0) {
                if (j == 0) return ret = s[0] != '+';
                return ret = s[0] != '-';
        }
        if (ret == -1) {
                if (j == 0) {
                        if (s[i] == '+') ret = get (i - 1, j);
                        else ret = get (i - 1, j ^ 1) + 1;
                } else {
                        if (s[i] == '-') ret = get (i - 1, j);
                        else ret = get (i - 1, j ^ 1) + 1;
                }
        }
        return ret;
}
int main () {
        #ifndef FILE_STREAM
        	#define fname "bb"
                freopen (fname".in", "r", stdin);
                freopen (fname".out", "w", stdout);
        #endif // FILE_STREAM
        int t; scanf ("%d\n", &t);
        for (int i = 1; i <= t; i++) {
                scanf ("%s\n", s); memset (dp, 255, sizeof (dp));
                printf ("Case #%d: %d\n", i, min (get (sz (s) - 1, 0), get (sz (s) - 1, 1) + 1));
        }
  	return 0;
}
