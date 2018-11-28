#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair <int,int> pii;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define gl(x) cin >> x
#define pl(x) cout << x
#define gi(x) scanf("%d", &x)
#define pi(x) printf("%d", x)
#define sz(a) (int)a.size()
#define all(c) c.begin(), c.end()
#define dbgn cerr << endl;
#define dbs(x) cerr << x << " "
#define dbg(x) cerr << #x << " : " << x << " "
#define rep(i, n) for(int i = 0; i < (n); i++)
#define rept(i, a, b) for(int i = (a); i < (b); i++)
#define fill(a, v) memset(a, v, sizeof(a))
#define foreach(c, it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

int f[111];

void add(int idx, int val) {
    while(idx < 111) {
        f[idx] += val;
        idx += idx & -idx;
    }
}

int get(int idx) {
    int sum = 0;
    while(idx > 0) {
        sum += f[idx];
        idx -= idx & -idx;
    }
    return sum;
}

int main() {
    clock_t start = clock();
    int cases;
    gi(cases);
    for(int caseN = 1; caseN <= cases; ++caseN) {
        int n; scanf("%d", &n);
        vi a(n);
        rep(i, n) gi(a[i]);
        vi b(a), srt(a);
        sort(all(srt));
        // rep(i, n) dbs(a[i]); dbgn;
        int maxn = srt[n - 1];
        map <int, int> hash;
        int lim = 1 << (n - 1);
        int ans = 11111111;
        rep(mask, lim) {
            vi left, right;
            rep(i, n - 1) {
                if(!(mask & (1 << i))) left.pb(srt[i]);
                else right.pb(srt[i]);
            }
            vi tmp;
            sort(all(left));
            sort(all(right));
            reverse(all(right));
            rep(i, sz(left)) tmp.pb(left[i]);
            tmp.pb(srt[n - 1]);
            rep(i, sz(right)) tmp.pb(right[i]);
            hash.clear();
            rep(i, n) hash[tmp[i]] = i + 1;
            rep(i, n) b[i] = hash[a[i]];
            int cur = 0;
            // rep(i, n) dbs(tmp[i]); dbgn;
            rep(i, n + 5) f[i] = 0;
            for(int i = n - 1; i >= 0; i--) {
                cur += get(b[i] - 1);
                add(b[i], 1);
            }
            ans = min(cur, ans);
        }
        printf("Case #%d: %d\n", caseN, ans);
    }
    fprintf(stderr, "Time Taken %.4lf\n", (clock() - start) / (double) CLOCKS_PER_SEC);
    return 0;
}