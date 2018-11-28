#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<VB> VVB;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef tr1::unordered_set<vector<bool> > MB;
typedef set<VVB> MVVB;
typedef map<int, VPII> MIVPII;
ifstream fin("input.in");
ofstream fout("output");
int N;

bool e(char c1, char c2) {
	return (c1 == c2) || (c1 == 'T') || (c2 == 'T');
}

class Test {
public:
	int N, M;
	VVI bd;
	VVI cb;
	MIVPII ib;

	Test(int n) {
		fin >> N >> M;
		bd.resize(N, VI(M));
		cb.resize(N, VI(M, 100));

		REP(i, N) {
			REP(j, M) {
				int h;
				fin >> h;
				bd[i][j] = h;
				cout << h;
				if (ib.find(h) == ib.end()) {
					ib[h] = VPII();
				}
				ib[h].pb(PII(i, j));
			}
			cout << endl;
		}

		cout << endl;

		fout << "Case #" << n << ": " << (cutFine() ? "YES" : "NO") << endl;
	}

	bool cutFine() {
		FOREACH(it, ib) {
			int h = it->X;
			VPII &pos = it->Y;
			FOREACH(it1, pos) {
				int x = it1->X, y = it1->Y;
				if (cb[x][y] > h) {
					// try horizontal cut
					if (canCutX(h, x)) {
						cutX(h, x);
					} else if (canCutY(h, y)) {
						cutY(h, y);
					} else {
						return false;
					}
				}
			}
		}
		return true;
	}

	bool canCutX(int h, int row) {
		REP(j, M) {
			if (bd[row][j] > h)
				return false;
		}
		return true;
	}

	bool canCutY(int h, int col) {
		REP(i, N) {
			if (bd[i][col] > h)
				return false;
		}
		return true;
	}

	bool cutY(int h, int col) {
		REP(i, N) {
			cb[i][col] = h;
		}
	}

	void cutX(int h, int row) {
		REP(j, M) {
			cb[row][j] = h;
		}
	}
};

int main() {
	cout << "starting" << endl;
	fin >> N;
	REP(i, N) {
		Test(i+1);
	}
}
