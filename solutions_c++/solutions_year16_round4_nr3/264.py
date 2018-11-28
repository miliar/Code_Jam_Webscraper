#define FNAME ""

#undef __STRICT_ANSI__

#include <bits/stdc++.h> 

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define fst first
#define snd second
#define sz(x) (int)((x).size()) 
#define forn(i,n) for (int i = 0; (i) < (n); ++i)
#define fornr(i,n) for (int i = (int)(n) - 1; (i) >= 0; --i)
#define forab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define forba(i,a,b) for (int i = (int)(b) - 1; (i) >= (a); --i)
#define forit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
	#define U64 "%I64u"
#else
	#define I64 "%lld"
	#define U64 "%llu"
#endif

typedef long long LL;
typedef unsigned long long ULL;
typedef double dbl;
typedef long double LD;
typedef unsigned int uint;
typedef pair <int, int> pii;
typedef vector <int> vi;

const int N = 100;

int step[2][4] = {{1, 0, 3, 2}, {3, 2, 1, 0}}, d[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int field[N][N], r, c;
vector <int> vis;

void dfs(int x, int y, int dd) {
//	cerr << x << " " << y << " " << dd << '\n';
	if (!x) {
		vis.pb(y);
		return;
	}
	if (!y) {
		vis.pb((2 * r + 2 * c) - x + 1);
		return;
	}
	if (x == r + 1) {
		vis.pb(2 * c + r - y + 1);
		return;
	}
	if (y == c + 1) {
		vis.pb(c + x);
		return;
	}
	dfs(x + d[step[field[x][y]][dd]][0], y + d[step[field[x][y]][dd]][1], step[field[x][y]][dd]);
}

int main() {
	int t;
	cin >> t;
	forn(q, t) {
		cin >> r >> c;
		cout << fixed << "Case #" << q + 1 << ":\n"; 
		vector <pii> pairs;
		forn(i, (r + c)) {
			int a, b; cin >> a >> b;
			pairs.pb(mp(a, b));
		}
		cerr << q + 1 << '\n';
		int flag = 0;
		forn(mask, (1 << (r * c))) {
			forn(i, r) {
				forn(j, c) {
					if (mask & (1 << (i * c + j))) 
						field[i + 1][j + 1] = 1;
					else
						field[i + 1][j + 1] = 0;
				} 
			}
	/*		cout << '\n';
			forn(i, r)  {
				forn(j, c)
 					cout << field[i + 1][j + 1] << " ";
				cout << '\n';
			}
			cout << '\n';
		*/	int ok = 1;
			forn(i, (r + c)) {
				vis.clear();
				int a = pairs[i].fst, b = pairs[i].snd;
		//		cerr << "a = " << a << '\n';
		//		cerr << "@\n";
				if (a <= c) {
					dfs(1, a, 1);
				}
		//		cerr << "@\n";
				if (a > c && a <= r + c) {
		//			cerr << "!\n";
					dfs(a - c, c, 2);
				}
		//		cerr << "@\n";
				if (a > r + c && a <= 2 * c + r) {
					dfs(r, c - (a - r - c) + 1, 3);
				}
		//		cerr << "@\n";
				if (a > 2 * c + r) {
					dfs(r - (a - 2 * c - r) + 1, 1, 0);
				}
				if (sz(vis) != 1 || vis[0] != b) {
	//				cerr << "sz = " << sz(vis) << '\n';
	//				if (sz(vis))
	//					cerr << "vis = " << vis[0] << '\n';
					ok = 0;
					break;
				}
			}
			if (ok) {
				forn(i, r) {
					forn(j, c) 
						if (field[i + 1][j + 1])
							cout << '/';
						else
							cout << '\\';
					cout << '\n';			
				}
				flag = 1;
				break;
			}
		}
		if (!flag)
			cout <<"IMPOSSIBLE\n";
	}
	return 0;
}
