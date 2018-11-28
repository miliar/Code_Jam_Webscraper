#include <bits/stdc++.h>
using namespace std;

#define repu(i, a, b) for (int i = (a); i < (b); ++i)
#define repd(i, a, b) for (int i = (a); i > (b); --i)
#define mem(a, x) memset(a, x, sizeof(a))
#define all(a) a.begin(), a.end()
#define uni(a) a.erase(unique(all(a)), a.end())
#define count_bits(x) __builtin_popcount(x)
#define count_bitsll(x) __builtin_popcountll(x)
#define least_bits(x) __builtin_ffs(x)
#define least_bitsll(x) __builtin_ffsll(x)
#define most_bits(x) 32 - __builtin_clz(x)
#define most_bitsll(x) 64 - __builtin_clz(x)

vector<string> split(const string &s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c)) v.push_back(x);
	return v;
}

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

void err(vector<string>::iterator it) {}

template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
	cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
	err(++it, args...);
}

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) {return (a < b) ? a : b;}
template<class T, class U> inline T tmax(T a, U b) {return (a > b) ? a : b;}
template<class T, class U> inline void amax(T &a, U b) {if (b > a) a = b;}
template<class T, class U> inline void amin(T &a, U b) {if (b < a) a = b;}
template<class T> inline T tabs(T a) {return (a > 0) ? a : -a;}
template<class T> T gcd(T a, T b) {while (b != 0) {T c = a; a = b; b = c % b;} return a;}

#define X first
#define Y second
typedef pair<int, int> P;
typedef pair<char, P> Q;
const int N = 105;
char b[N][N];
int R, C, ans;
bool mark[N][N];

const char tt[] = {'>', '<', '^', 'v'};

void f(int &x, int &y, char d) {
	if (d == '>') y++;
	if (d == '<') y--;
	if (d == '^') x--;
	if (d == 'v') x++;
}

bool inside(int x, int y) {
	return x >= 0 && x < R && y >= 0 && y < C;
}

bool go(int x, int y, vector<Q> &dir) {
	mem(mark, 0);
	while (true) {
		if (mark[x][y]) return true;
		mark[x][y] = 1;
		if (b[x][y] != '.') {
			dir.push_back(Q(b[x][y], P(x, y)));
			f(x, y, b[x][y]);
			if (!inside(x, y)) return false;
		}
		else {
			f(x, y, dir.back().X);
			if (!inside(x, y)) return false;
		}
	}
}

char opposite(char x) {
	if (x == '<') return '>';
	else if (x == '>') return '<';
	else if (x == 'v') return '^';
	else return 'v';
}

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);
    
	int ntest;
	
	cin >> ntest;
	repu(t, 1, ntest + 1) {
		cin >> R >> C;
		repu(i, 0, R) cin >> b[i];
		
		bool good = 1;
		ans = 0;
		repu(i, 0, R) repu(j, 0, C) {
			if (b[i][j] != '.') {
				vector<Q> rec;
				if (!go(i, j, rec)) {
					if (rec.size() >= 2) {
						Q &q1 = rec[rec.size() - 1];
						Q &q2 = rec[rec.size() - 2];
						b[q1.Y.X][q1.Y.Y] = opposite(q2.X);
						ans++;
					}
					else {
						char cc = b[i][j];
						bool found = 0;
						repu(k, 0, 4) {
							if (tt[k] == cc) continue;
							rec.clear();
							b[i][j] = tt[k];
							if (go(i, j, rec)) {
								found = 1;
								break;
							}
						}
						if (found) ans++;
						else {
							repu(k, 0, 4) {
								if (tt[k] == cc) continue;
								rec.clear();
								b[i][j] = tt[k];
								go(i, j, rec);
								if (rec.size() >= 2) {
									Q &q1 = rec[rec.size() - 1];
									Q &q2 = rec[rec.size() - 2];
									b[q1.Y.X][q1.Y.Y] = opposite(q2.X);
									ans += 2; found = 1;
									break;
								}
							}
						}
						if (!found) good = 0;
					}
				}
			}
		}
		if (!good) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, ans);
	}
    return 0;
}
