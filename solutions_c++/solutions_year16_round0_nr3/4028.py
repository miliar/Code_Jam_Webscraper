#include <bits/stdc++.h>

#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define sz(s) ((int) s.size ())
#define all(s) s.begin (), s.end ()
#define seed srand (chrono :: duration_cast<chrono :: nanoseconds> (chrono :: high_resolution_clock :: now().time_since_epoch ()).count ())
#define rand ((rand () << 16) ^ (rand ()))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

const int N = 19;
const int inf = (int) 2e9;
const ll linf = (ll) 9e18;
const int mod = (int) 1e9 + 7;

int n = 16;
int j = 50;

int a[N];

ll prime (ll x) {
        ll sq = (ll) sqrt ((double) x);
        for (ll i = 2; i <= sq; i++) if (x % i == 0) return i;
        return -1;
}
void gen (int k) {
        if (j <= 0) exit (0);
        if (k == n) {
                vector<ll> v;
                for (int b = 2; b <= 10; b++) {
                        ll r = 0;
                        for (int i = 0; i < n; i++) r = r * b + a[i];
                        if ((r = prime (r)) == -1) return;
                        v.pb (r);
                }
                --j;
                for (int i = 0; i < n; i++) printf ("%d", a[i]);
                for (int i = 0; i < 9; i++) printf (" %d", v[i]);
                printf ("\n");
        } else for (int i = 1; i >= (k == n - 1 || k == 0); i--) a[k] = i, gen (k + 1);
}
int main () {
        #ifdef FILE_STREAM
        	#define fname ""
                freopen (fname".in", "r", stdin);
                freopen (fname".out", "w", stdout);
        #endif // FILE_STREAM
        puts ("Case #1:");
        gen (0);
  	return 0;
}
