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

int w[10010];

int main() {
    int cases;
    gi(cases);
    for(int caseN = 1; caseN <= cases; ++caseN) {
        int n, x;
        gi(n); gi(x);
        rep(i, n) gi(w[i]);
        sort(w, w + n);
        int st = 0, en = n - 1;
        int discs = 0;
        while(st < en) {
            if(w[st] + w[en] > x) {
                ++discs;
                --en;
            } else {
                ++st;
                --en;
                ++discs;
            }
        }
        if(st == en) {
            ++discs;
        }
        printf("Case #%d: %d\n", caseN, discs);
    }
    return 0;
}