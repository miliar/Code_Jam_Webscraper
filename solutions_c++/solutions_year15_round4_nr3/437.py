#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
//const ld PI = acosl(ld(-1));

const int N = 200 + 13;

int n;
vector<li> sent[N];

inline li has(string& s) {
	li res = 0;
	forn(i, sz(s)) {
		res = res * 1009 + s[i];
	}
	return res;
}

vector<li> readSent() {
	vector<li> res;
	string s;
	string cur = "";
	getline(cin, s);
	s += " ";
	forn(i, sz(s)) {
		if (s[i] == ' ') {
			if (sz(cur))
				res.pb(has(cur));
			cur = "";
		} else {
			cur += s[i];
		}
	}
	return res;
}

inline bool read() {
	assert(scanf("%d ", &n) == 1);
	forn(i, n) {
		sent[i] = readSent();
	}
    return true;
}

int us;

unordered_map< li, int > words;
unordered_set<li> ft;
unordered_set<li> sc;

inline void solve(int test) {
	ft.clear();
	sc.clear();
	words.clear();
	forn(i, n) {
		forn(j, sz(sent[i])) {
			words[sent[i][j]] = -2;
		}
	}
	forn(j, sz(sent[0])) {
		ft.insert(sent[0][j]);
	}
	forn(j, sz(sent[1])) {
		sc.insert(sent[1][j]);
	}
	vector<li> ss;
	for(auto it = words.begin(); it != words.end(); it++) {
		if (ft.count(it->ft) && sc.count(it->ft))
			ss.pb(it->ft);
	}
	
	forn(i, sz(ss)) 
		words.erase(ss[i]);

	int ans = INF;
	forn(mask, 1 << n) {
//	fore(mask, 14, 14) {
		if (!((mask & 1) == 0 && ((mask >> 1) & 1) == 1))
			continue;
		int cur = 0;
		
		vector<string> ss;
		fore(i, 2, n - 1) {
			if (mask & (1 << i))
				continue;
			forn(j, sz(sent[i])) {
				if (!words.count(sent[i][j]))
					continue;
				words[sent[i][j]] = mask;
			}
		}
		fore(i, 2, n - 1) {
			if (mask & (1 << i))
				continue;
			forn(j, sz(sent[i])) {
				if (!words.count(sent[i][j]))
					continue;
				if (words[ sent[i][j] ] == mask && ft.count(sent[i][j])) {
					words[sent[i][j]] = -2;
					cur++;
				}
			}
		}
		fore(i, 2, n - 1) {
			if (!(mask & (1 << i)))
				continue;
			forn(j, sz(sent[i])) {
				if (!words.count(sent[i][j]))
					continue;
							
				if (words[ sent[i][j] ] == -mask)
					continue;
					
				if (sc.count(sent[i][j]) || words[ sent[i][j] ] == mask) {
					words[sent[i][j]] = -mask;
					cur++;
				}
			}
		}
//		cerr << (mask >> 2) << " " << cur << endl;
		ans = min(ans, cur);
	}
	printf("Case #%d: %d\n", test, ans + sz(ss));
}

int main()
{
#ifdef SU2_PROJ
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
#endif

    cout << setprecision(25) << fixed;
    cerr << setprecision(10) << fixed;

    srand(int(time(NULL)));

    int n;
    assert(scanf("%d", &n) == 1);
    
    forn(i, n) {
	    assert(read());
    	solve(i + 1);
    	cerr << i + 1 << " TIME: " << clock() << endl;
    }

#ifdef SU2_PROJ
    cerr << "TIME: " << clock() << endl;
#endif

    return 0;
}