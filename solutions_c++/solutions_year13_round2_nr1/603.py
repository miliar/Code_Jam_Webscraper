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
typedef vector<double> VD;

auto space = boost::is_any_of(" ");
ifstream fin;
ofstream fout;

//while (getline(fin, line)) {
//	split(vs, line, space);


class Test {
public:
	Int N;
	Int si;
	VInt s;

	Test(int n) {
		fin >> si >> N;
		s.resize(N);

		REP(i, N) {
			fin >> s[i];
		}

		fout << "Case #" << n << ": ";
		SORT(s);

		Int current = si;
		Int opt = 0;

		cout << "n = " << n << endl;
		if (si == 1) {
			opt = N;
		} else {
			REP(i, N) {
				Int left = N - i;
				//cout << format("current = %d, s[%d] = %d") % current % i % s[i] << endl;
				if (current <= s[i]) {
					Int opt1 = getAll(current, i);
					//cout << "smaller" << endl;
					if (opt1 > left) {
						//cout << "left" << endl;
						opt += left;
						break;
					} else {
						while (current <= s[i]) {
							current += current - 1;
							opt++;
						}
						//cout << "opt = " << opt << endl;
						current += s[i];
					}
				} else {
					//cout << "not smaller" << endl;
					current += s[i];
				}
				//cout << format("i = %d, cs = %d") % i % current << endl;
			}
		}
		fout << opt << endl;
	}

	Int getAll(Int c, Int index) {
		Int opt1 = 0;
		Int t1 = c;
		FOR(i, index, N) {
			while (t1 <= s[i]) {
				t1 += t1 - 1;
				opt1++;
			}
			t1 += s[i];
		}
		return opt1;
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
	FOR(i, 1, T + 1) {
		Test t(i);
	}
}
