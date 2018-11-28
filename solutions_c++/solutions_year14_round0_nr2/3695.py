#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>
#include <valarray>
#include <cmath>
#include <climits>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
// #define cpp11
#ifdef cpp11
	#include <unordered_map>
	#include <unordered_set>
	#include <regex>
	#include <tuple>
	#include <cstdint>
#endif

using namespace std;

//#define DO_DEBUG 1

#define INFIN 0x3f3f3f3f
#define cin fin
#define cout fout

int N;
ofstream fout ("b.out");
ifstream fin ("B-large.in");

int main() {
	cin >> N;
	for (int n = 1; n <= N; n++) {
		double C, F, X;
		cin >> C >> F >> X;
		double c = 0, t = 0, r = 2;
		while (1) {
			t += C/r;
			double tleft = (X-C)/r;
			double nt = X/(r+F);
			if (tleft < nt) {
				cout << "Case #" << n << ": " << setprecision(32) << t + tleft << '\n';
				goto EndOfCase;
			}
			else r += F;
		}
		EndOfCase: continue;
	}
	return 0;
}