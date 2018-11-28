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

const int N = 2005, M = 10;

int T, n;
char s[N];
int c[M], k[26];
string str[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string ans = "ZGXWURFOSI";
int id[10] = {0, 8, 6, 2, 4, 3, 5, 1, 7, 9};

int main() {
    file_r("A-large.in");
    file_w("A-large.out");
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", s);
        n = strlen(s);
        memset(c, 0, sizeof(c));
        memset(k, 0, sizeof(k));
        rep (i, n) k[s[i] - 'A']++;
        rep (i, 10) {
            c[id[i]] = k[ans[i] - 'A'];
            //sc2(id[i], c[id[i]]);
            repit (it, str[id[i]]) k[*it - 'A'] -= c[id[i]];
        }
        printf("Case #%d: ", ++cas);
        rep (i, 10) rep (j, c[i]) printf("%d", i);
        puts("");

//        sort(s, s + n);
//        cout << s << '\n';
//        string hh;
//        rep (i, 10) rep (j, c[i]) rep (l, SZ(str[i])) hh.pb(str[i][l]);
//        sort(ALL(hh));
//        cout << hh << '\n';
//        string dd = s;
//        if (dd != hh) cout << "FUCK!!!!!!!!!!!!!!!!!!!!!!" << '\n';
    }
    return 0;
}
















