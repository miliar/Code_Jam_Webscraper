#ifdef MG
#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
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

template<typename X> inline X abs(const X &a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X &a) { return a * a; }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const pair <X, Y>& p) { return out << '(' << p.x << ", " << p.y << ')'; }
template<typename X> inline ostream& operator<< (ostream& out, const vector<X>& p) { forn(i, sz(p)) { if (i != 0) out << ' '; out << p[i]; } return out; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = acosl(ld(-1));

const int N = 100 + 13;

int n, k;
string s;

const int ALP = 260;
int q[ALP];

inline bool read()
{
	char buf[N];
	int l;
	
	if (scanf("%d%d%d", &k, &l, &n) != 3) return false;
	
	assert(scanf("%s", buf) == 1);
	string letters;
	letters = string(buf);
	memset(q, 0, sizeof q);
	forn(i, sz(letters))
		q[int(letters[i])]++;
	
	assert(scanf("%s", buf) == 1);
	s = string(buf);
	
	return true;
}

int p[N];
int next[N][ALP];

inline void prepare()
{
	s += '#';
	memset(p, 0, sizeof p);

	forl(i, sz(s) - 1) {
		int j = p[i - 1];
		while (j > 0 && s[i] != s[j]) j = p[j - 1];
		if (s[i] == s[j]) j++;
		p[i] = j;
	}
	
    memset(next, 0, sizeof next);
    
    forn(i, sz(s))
    	for (int c = 'A'; c <= 'Z'; c++)
    		if (i > 0 && c != s[i])
    			next[i][c] = next[p[i - 1]][c];
    		else
    			next[i][c] = i + int(c == s[i]);
    			
    s.erase(--s.end());
}

int u, used[N][N][N];
ld z[N][N][N];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	prepare();
	
	memset(z, 0, sizeof z);
	
	u++;
	used[0][0][0] = u;
	
	z[0][0][0] = 1;
	
	forn(i, n)
		forn(j, sz(s) + 1)
			forn(cnt, n + 1)
			{
				if (used[i][j][cnt] != u) continue;
				const ld &dv = z[i][j][cnt];
				
				for (int p = 'A'; p <= 'Z'; p++)
				{
					if (q[p] == 0) continue;
					
					int ni = i + 1, nj = next[j][p], ncnt = cnt + (nj == sz(s));
					z[ni][nj][ncnt] += dv * q[p] / ld(k);
					used[ni][nj][ncnt] = u;
				}
			}
			
	int maxv = 0;
	forn(j, sz(s) + 1)
		forn(cnt, n + 1)
			if (used[n][j][cnt] == u)
				maxv = cnt;
				
	//cerr << maxv << endl;
				
	ld ans = 0;
	forn(j, sz(s) + 1)
		forn(cnt, n + 1)
			if (used[n][j][cnt] == u)
				ans += z[n][j][cnt] * (maxv - cnt);
				
	printf("%.10lf\n", double(ans));
}

int main()
{
#ifdef MG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int T;
	cin >> T;
	
	forn(t, T)
	{
		assert(read());
		solve(t);
	}
	
#ifdef MG
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
