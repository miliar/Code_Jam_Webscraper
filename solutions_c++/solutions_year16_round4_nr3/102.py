#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = 1E9;	
const int MAXN = 100500;
const pii d[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int tt, n, m, N;
int tmr;
vector<pii> need;
string s[MAXN];
vector<int> g[MAXN];
int used[MAXN];

int getId(int sq, int side) {
	return sq * 4 + side;	
}

void addEdge(int s1, int q1, int s2, int q2) {
	int v = getId(s1, q1);
	int w = getId(s2, q2);
	g[v].pb(w);
	g[w].pb(v);
}

int cellId(int i, int j) {
	return i * m + j;	
}

bool correct(int i, int j) {
	return 0 <= i && i < n && 0 <= j && j < m;	
}

int getBoundId(int num) {
	if (num < m)
		return getId(cellId(0, num), 0);
	num -= m;
	
	if (num < n)
		return getId(cellId(num, m - 1), 1);
	num -= n;
	
	if (num < m)
		return getId(cellId(n - 1, m - 1 - num), 2);
	num -= m;
	
	if (num < n)
		return getId(cellId(n - 1 - num, 0), 3);
	num -= n;
	
	assert(false);
}

void dfs(int v) {
	used[v] = tmr;
	for (auto w: g[v])
		if (used[w] != tmr)
			dfs(w);	
}

int main() {
	
	cin >> tt;
	forn(ttt, tt) {
		cin >> n >> m;
		printf("Case #%d:\n", ttt + 1);

		N = n * m;
		need.clear();
		
		need.resize(n + m);
		forn(i, n + m) {
			scanf("%d%d", &need[i].X, &need[i].Y);
			need[i].X--;
			need[i].Y--;
		}
		
		forn(i, n) {
			s[i] = "";
			forn(j, m)
				s[i] += ' ';
		}
		/*
		cout << n << ' ' << m << '\n';
		forn(i, 2 * (n + m))
			cout << getBoundId(i) << '\n';
		*/	
		bool OK = 0;
		forn(mask, 1 << N) {
			int M = mask;
			
			forn(i, n)
				forn(j, m) {
					int b = (M & 1);
					s[i][j] = (b ? '/' : '\\');
					M >>= 1;
				}
				                              
			//build graph
			int MAXID = N * 10;
			forn(i, MAXID)
				g[i].clear();
				
			forn(i, n)
				forn(j, m) {
					if (s[i][j] == '/') {
						addEdge(cellId(i, j), 1, cellId(i, j), 2);
						addEdge(cellId(i, j), 0, cellId(i, j), 3);
					} else {
						addEdge(cellId(i, j), 0, cellId(i, j), 1);
						addEdge(cellId(i, j), 2, cellId(i, j), 3);
					}						
				}
				
			forn(i, n)
				forn(j, m) {
					forn(dd, 4) {
						int ni = i + d[dd].X;
						int nj = j + d[dd].Y;

						if (correct(ni, nj)) {
							addEdge(cellId(i, j), dd, cellId(ni, nj), (dd + 2) % 4);
						}
					}
				}

			forn(i, MAXID)
				used[i] = 0;
			tmr = 1;
				
			bool con = 1;
			for (auto p: need) {
				int v = getBoundId(p.X);
				int w = getBoundId(p.Y);
				tmr++;
				
				dfs(v);
				if (used[w] != tmr) {
					con = 0;
					break;
				}
			}
			
			if (con) {
				OK = 1;
				break;
			}				
		}
		
		if (!OK) {
			cout << "IMPOSSIBLE\n";	
		} else {
			forn(i, n)
				cout <<	s[i] << '\n';
		}
	}
		
	return 0;
}                