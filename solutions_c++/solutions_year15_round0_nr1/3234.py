#include <bits/stdc++.h>

#define file_r(x) freopen(x,  "r",  stdin)
#define file_w(x) freopen(x,  "w",  stdout)
#define rep(i, n) for (int i = 0; i < n; i++)
#define FOR(i, n, m) for (int i = n; i <= m; i++)
#define repe(i, u) for (int i = head[u]; ~i; i = nxt[i])
#define FORD(i, n, m) for (int i = n; i >= m; i--)
#define repit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pause cout << " press ant key to continue...", cin >> chh

#define pb push_back
#define mp make_pair
#define ins insert
#define X first
#define Y second
#define be begin
#define nb rbegin
#define er erase
#define SZ(c) c.size()
#define ins insert

#define sc(n) cout << #n << "= " << n, system("pause")
#define sc2(n, m) cout << #n << "= " << n << " " << #m << "= " << m, system("pause")
#define sc3(n, m, k) cout << #n << "= " << n << " " << #m << "= " << m << " " << #k << "= " << k, system("pause")
#define sc4(n, m, k, b) cout << #n << "= " << n << " " << #m << "= " << m << " " << #k << "= " << k << " " << #b << "= " << b, system("pause")

using namespace std;
int chh;

const int N = 1005;

int T, n;
char s[N];

int main() {
    file_r("A-large.in");
    file_w("A-large.out");
    int now, tmp, cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %s", &n, s);
        now = 0, tmp = 0;
        rep (i, n + 1) {
            if (now >= i) {
                now += s[i] - '0';
            } else {
                tmp += i - now;
                now = i;
                now += s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", ++cas, tmp);
    }
    return 0;
}







