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

const int N = 10 * 1000 + 13;

int n, rep;
char s[N];

inline bool read()
{
    if (scanf("%d%d", &n, &rep) != 2) return false;
    assert(scanf("%s", s) == 1);
    int on = n;
    forn(iter, rep - 1) forn(i, on) s[n++] = s[i];
	return true;
}

const char cc[3] = {'i', 'j', 'k'};

inline int getp (char c)
{
    forn(i, 3) if (cc[i] == c) return i;
    throw;
}

inline pair<int, char> mult (const pair<int, char>& a, const pair<int, char>& b)
{
    pair<int, char> result(a.first * b.first, '1');
    if (a.sc == '1') result.sc = b.sc;
    else if (b.sc == '1') result.sc = a.sc;
    else if (a.sc == b.sc) result.ft *= -1;
    else
    {
        int p1 = getp(a.sc), p2 = getp(b.sc);
        if (p2 == (p1 + 1) % 3) result.sc = cc[(p1 + 2) % 3];
        else result.sc = cc[(p1 + 1) % 3], result.ft *= -1;
    }
    return result;
}

inline pair<int, char> calc(int lf, int rg)
{
    pair<int, char> result(1, '1');
    fore(i, lf, rg) result = mult(result, mp(1, s[i]));
    return result;
}

inline void solve()
{
    pair<int, char> final(1, '1');
    forn(i, n) final = mult(final, mp(1, s[i]));
    if (final != mp(-1, '1'))
    {
        puts("NO");
        return;
    }
    pair<int, char> ltor(1, '1');
    int firsti = -1;
    forn(i, n)
    {
        ltor = mult(ltor, mp(1, s[i]));
        if (ltor == mp(1, 'i'))
        {
            firsti = i;
            break;
        }
    }
    if (firsti == -1)
    {
        puts("NO");
        return;
    }

    pair<int, char> rtol(1, '1');
    for (int i = n - 1; i > firsti; i--)
    {
        rtol = mult(mp(1, s[i]), rtol);
        if (rtol == mp(1, 'k'))
        {
            assert(calc(firsti + 1, i - 1) == mp(1, 'j'));
            puts("YES");
            return;
        }
    }

    puts("NO");
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;

    char ccc[4] = {'1', 'i', 'j', 'k'};
    forn(i, 4)
    {
        forn(j, 4) cerr << mult(mp(1, ccc[i]), mp(1, ccc[j])) << ' ';
        cerr << endl;
    }

	int testCount;
	cin >> testCount;

	forl(test, testCount)
	{
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
