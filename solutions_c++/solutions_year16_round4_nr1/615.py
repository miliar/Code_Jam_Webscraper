#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <utility>
#include <numeric>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)
#define kep(i, n) for (int i = 1; i <=n; ++i)
#define fo(i, l, r) for (int i = l; i <= r; ++i)
#define fd(i, r, l) for (int i = r; i >= l; --i)
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define mp make_pair
#define pb push_back

int T, n, rr, pp, ss;
const string cc = "PRS";
const string sc[] = {"PR", "RS", "PS"};
int ff[1111];

int cnt(string s, char c) {
    int ans = 0;
    rep(i, (int)s.size()) if (s[i] == c) ++ans;
    return ans;
}

string make(int d, int x) {
    if (d == 1) return sc[x];
    else {
        string s1 = make(d-1, ff[sc[x][0]]), s2 = make(d-1, ff[sc[x][1]]);
        return min(s1+s2, s2+s1);
    }
}

void solve() {
    scanf("%d%d%d%d", &n, &rr, &pp, &ss);
    int s[3], sn[3];
    rep(i, 3) {
        s[0] = s[1] = s[2] = 0;
        s[i] = 1;
        rep(j, n) {
            sn[0] = sn[1] = sn[2] = 0;
            rep(k, 3) rep(t, 2)
                sn[ff[(int)sc[k][t]]] += s[k];
            rep(k, 3) s[k] = sn[k];
        }
        if (s[0] == pp && s[1] == rr && s[2] == ss) {
            puts(make(n, i).c_str());
            return;
        }// else {printf("%d:%d:%d\n", s[0], s[1], s[2]);}
    }
    puts("IMPOSSIBLE");
}

int main() {
    memset(ff, 0, sizeof(ff));
    ff['P'] = 0;
    ff['R'] = 1;
    ff['S'] = 2;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
}
