#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)

#define pause cout << " press ansy key to continue...",  cin >> chh
#define file_r(x) freopen(x,  "r",  stdin)
#define file_w(x) freopen(x,  "w",  stdout)
#define lowbit(x) ((x) & (-x))
#define repit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i, n) for (int i = 0; i < (n); i++)
#define repe(i, u) for (int i = head[u]; i != -1; i = nxt[i])
#define repd(i, n) for (int i = (n - 1); i >= 0; i--)
#define FOR(i, n, m) for (int i = (n); i <= (m); i++)
#define FORD(i, n, m) for (int i = (n); i >= (m); i--)
#define pb push_back
#define X first
#define Y second
#define ins insert
#define rb rbegin
#define be begin
#define er erase
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define SZ(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define sqr(r) ((LL) (r) * (r))
#define dis(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define FASTIO ios::sync_with_stdio(false);cin.tie(0)

#define sc(x) cout << #x" = " << x << endl, system("pause")
#define sc2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl, system("pause")
#define sc3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl, system("pause")
#define sc4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl, system("pause")

#define in(n) scanf("%d", &n)
#define in2(n, m) scanf("%d %d", &n, &m)
#define in3(x, y, z) scanf("%d %d %d", &x, &y, &z)

using namespace std;
int chh;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef pair<int, pii> pi3;
typedef vector< pair<int, int> > vpii;
typedef long long LL;

const int N = 31, M = 1005;

int T, n;
int a[N];

int main() {
    file_r("A-large.in");
    file_w("A-small.out");
    int cas = 0, m0, m1, x, c;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        FOR (i, 1, n) scanf("%d", &a[i]);
        printf("Case #%d:", ++cas);
        while (1) {
            x = -1, m0 = -1, m1 = -1, c = 0;
            FOR (i, 1, n) {
                if (a[i] > x) x = a[i], m0 = i, m1 = -1, c = 1;
                else if (a[i] == x) m1 = i, c++;
            }
            if (x == 0) break;
            cout << ' ';
            if (x == 1 && c == 3) cout << char(m0 + 'A' - 1), a[m0]--;
            else {
                if (m0 != -1) cout << char(m0 + 'A' - 1), a[m0]--;
                if (m1 != -1) cout << char(m1 + 'A' - 1), a[m1]--;
            }
            int sum = 0;
            FOR (i, 1, n) sum += a[i];
            FOR (i, 1, n) if (a[i] * 2 > sum) puts("FUCK");
        }
        puts("");
    }
    return 0;
}













