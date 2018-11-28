#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair
#define fs first
#define sc second

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;

int n;
char s[1010];
vector<int> ept[1010];
vector<pair<char, int> > now[1010];

void solve() {
    cin >> n;
    forn(i, 105)
        now[i].clear(), ept[i].clear();

    forn(i, n) {
        scanf("%s", s);
        int yl = 0;
        while (s[yl] != '\0') {
            int cnt = 0;
            while (s[yl] != '\0' && s[yl] == s[yl + 1])
                yl++, cnt++;
            now[i].pb(mp(s[yl], cnt));
            yl++;
        }
    }

    forn(i, n) {
        if (now[i].size() != now[0].size()) {
            cout << "Fegla Won" << endl;
            return;
        }
        forn(j, now[i].size())
            if (now[i][j].fs != now[0][j].fs) {
                cout << "Fegla Won" << endl;
                return;
            } else {
                ept[j].pb(now[i][j].sc);
            }
    }

    int ans = 0;
    forn(i, now[0].size()) {
        int best = 100000000;
        forn(f, 105) {
            int now = 0;
            forn(j, ept[i].size())
                now += abs(f - ept[i][j]);
            best = min(best, now);
        }
        ans += best;
    }
    cout << ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

	return 0;
}
