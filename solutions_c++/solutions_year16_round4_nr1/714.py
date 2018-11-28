#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define foreach(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const pair <X, Y>& p) { return out << '(' << p.x << ", " << p.y << ')'; }
template<typename X> inline ostream& operator<< (ostream& out, const vector<X>& p) { forn(i, sz(p)) { if (i != 0) out << ' '; out << p[i]; } return out; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

int n, source[3];

inline bool read() {
    if (scanf("%d", &n) != 1) return false;
    forn(i, 3) assert(scanf("%d", &source[i]) == 1);
	return true;
}

int idx[300];

inline string getNext(char c) {
    if (c == 'R') return "RS";
    if (c == 'S') return "SP";
    if (c == 'P') return "PR";
    throw;
}

inline string gen(char startC) {
    string cur;
    cur.pb(startC);
    forn(iter, n) {
        string next;
        forn(i, sz(cur)) {
            next += getNext(cur[i]);
        }
        cur = next;
    }
    return cur;
}

string mySort(const string& s) {
    if (sz(s) == 1) return s;
    string s1 = s.substr(0, sz(s) / 2);
    string s2 = s.substr(sz(s) / 2);

    s1 = mySort(s1);
    s2 = mySort(s2);

    if (s1 + s2 > s2 + s1) swap(s1, s2);

    return s1 + s2;
}

inline void solve() {
    idx['R'] = 0;
    idx['P'] = 1;
    idx['S'] = 2;
    char start[] = {'R', 'P', 'S'};
    string ans = "";
    forn(iter, 3) {
        string res = gen(start[iter]);
        res = mySort(res);
        //std::cerr << res << endl;
        int cnt[3] = {0, 0, 0};
        forn(i, sz(res)) {
            cnt[idx[res[i]]]++;
        }
        bool good = true;
        forn(i, 3) if (cnt[i] != source[i]) { good = false; }
        if (good) {
            if (ans.empty() || ans > res) ans = res;
        }
    }
    if (ans.empty()) ans = "IMPOSSIBLE";
    puts(ans.c_str());
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;

	int testCount;
	cin >> testCount;

	forl(test, testCount) {
#ifdef SU2_PROJ
		cerr << "=== test: " <<  test << ", time: " << clock() / CLOCKS_PER_SEC << " ===" << endl;
#endif
		assert(read());
		printf("Case #%d: ", test);
		solve();
	}
	
#ifdef SU2_PROJ
	cerr << "=== TOTAL TIME: " << clock() / CLOCKS_PER_SEC << " ===" << endl;
#endif

	return 0;
}
