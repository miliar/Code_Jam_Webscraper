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
#include <unordered_map>
#include <unordered_set>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/format.hpp>
#include <NTL/ZZ.h>
#include <NTL/RR.h>

using namespace std;
using namespace NTL;
using boost::lexical_cast;
using boost::split;
using boost::format;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
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
typedef unordered_set<vector<bool> > MB;
typedef map<char, PII> MCPII;
typedef long long Int;
typedef vector<Int> VInt;
typedef vector<VInt> VVInt;
typedef vector<double> VD;

auto space = boost::is_any_of(" ");
ifstream fin;
ofstream fout;

//while (getline(fin, line)) {
//	split(vs, line, space);

VVInt C;

void FillC(int N) {
	C.resize(N + 1, VInt(N + 1, 0));
	C[0][0] = 1;
	FOR(i, 1, N) {
		C[i][0] = 1;
		FOR(j, 0, i + 1) {
			if (j == 0)
				C[i][0] = 1;
			else {
				C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
			}
			//cout << format("C[%d][%d] = %d") % i % j % C[i][j] << endl;
		}
	}
}

Int Fn(Int x) {
	return (x + 1) * (2 * x + 1);
}
class Test {
public:
	Int N, x, y;

	Test(int n) {
		fin >> N >> x >> y;

		fout << "Case #" << n << ": ";
		if (x < 0)
			x = -x;

		Int total = x + y;
		double ans = 0;
		if (total % 2 == 0) {
			Int nth = total / 2;

			if (x == 0) {
				Int fn = Fn(nth);
				if (N >= fn) {
					ans = 1;
				}
			} else {
				Int fn = Fn(nth - 1);
				if (N > fn) {
					Int np = N - fn;
					if (np >= total + y + 1) {
						ans = 1;
					} else if (np >= y + 1) {
						double t1 = 1;
						REP(i, y + 1) {
							t1 *= 0.5;
						}
						FOR(k, 0, np - y) {
							cout << "here" << endl;
							cout << t1 << endl;
							ans += t1 * C[y + k][k];
							t1 *= 0.5;
						}
					}
				}
			}
		}
		fout << ans << endl;
	}
};

int main(int argc, char *argv[]) {
	int T;
	string name = argv[1];
	string file_in = name + ".in";
	string file_out = name + ".out";
	fin.open(file_in);
	fout.open(file_out);
	cout << format("Input file = %s, Output file = %s") % file_in % file_out << endl;
	fin >> T;
	cout << "Number of test cases: " << T << endl;
	FillC(5000);
	FOR(i, 1, T + 1) {
		Test t(i);
	}
}
