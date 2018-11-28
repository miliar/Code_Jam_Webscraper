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
using namespace std;
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
typedef set<VVB> MVVB;
typedef map<char, PII> MCPII;
using boost::split;
typedef long long Int;
auto space = boost::is_any_of(" ");
ifstream fin("input.in");
ofstream fout("output");
int N;

//while (getline(fin, line)) {
//	split(vs, line, space);

class Test {
public:
	Int r, t;

	Test(int n) {
		fin >> r >> t;
		Int sum = 0, i = 0;
		while (sum <= t) {
			sum += 2 * (r + 2 * i) + 1;
			i++;
		}
		--i;

		fout << "Case #" << n << ": " << i << endl;
	}
};

int main() {
	cout << "starting" << endl;
	fin >> N;
	REP(i, N) {
		Test t(i+1);
	}
}
