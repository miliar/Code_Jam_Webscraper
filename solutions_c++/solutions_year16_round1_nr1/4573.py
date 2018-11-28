#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
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
#include <unistd.h>
#include <cassert>
#include <memory.h>
#include <limits>

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
typedef vector<PII> VPII;
typedef vector<VI> VVI;

#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define TIMESTAMPf(x,...) eprintf("[" x "] Time : %.3lf s.\n", __VA_ARGS__, clock()*1.0/CLOCKS_PER_SEC)

inline void PreCalc() {
}

#define SMALL
//#define LARGE

void solve() {
	string s;
	static char buf[1000];
	scanf("%s", buf);
	s = buf;

	vector<string> stack;
	vector<string> temp;
	if (s.length() == 1) {
		cout << s << endl;

	} else {
		stack.push_back(s.substr(0, 1));
			for(int index = 1 ; index < (int)s.length(); index++) {
				temp.clear();
				REP(i , stack.size()) {
					temp.push_back(s[index] + stack[i]);
					temp.push_back(stack[i] + s[index]);
				}
				stack = temp;
				if (index == ((int)s.length() - 1)) {
					SORT(stack);
		//			REP(i , stack.size()) {
						cout << stack[stack.size() - 1] << " ";
		//			}
				}
			}

			cout  << endl;
	}

}

int main() {
	PreCalc();
	TIMESTAMP(PreCalc);

	string inputFile = "A-small-attempt0.in";
	string outputFile = "A-small-attempt0.txt";
	freopen(inputFile.c_str(), "r", stdin);
	freopen(outputFile.c_str(), "w+", stdout);

	int testNum;
	scanf("%d", &testNum);

	for (int testId = 1; testId <= testNum; testId++) {
		printf("Case #%d: ", testId);
		solve();
	}

	TIMESTAMP(end);

	return 0;
}
