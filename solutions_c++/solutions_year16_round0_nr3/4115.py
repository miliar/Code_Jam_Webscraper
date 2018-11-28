#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <memory>
#include <unordered_set>
#include <unordered_map>
#include <iterator>
#include <deque>
#include <queue>
#include <cmath>
#include <functional>
#include <numeric>
#include "stdio.h"
#include "time.h"
#include <climits>
#include <stdio.h> 
#include <tuple>
#include <fstream>

#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

//#include <boost/lexical_cast.hpp>
//#include <boost/filesystem.hpp>
//#include <boost/utility.hpp>
//#include <boost/aligned_storage.hpp>
//<boost/align/alignment_of.hpp>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORD(i,a,b) for (int i = (a); i > (b); --i)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define ABS(a) (((a) >= 0) ? (a) : -(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))


using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<vector<pair<int, int> > > VVPI;

const double EPS = 1e-8;

void init() {
#ifdef SAMMAX
	//#include "MathFuncs.h"
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	beg = clock();
#else
	//std::ios_base::sync_with_stdio(false);
	//std::cin.tie(nullptr);
	//freopen("kimbits.in", "r", stdin);
	//freopen("kimbits.out", "w", stdout);
#endif  
}

void finish() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}

int gcd(int a, int b) { return !a ? b : gcd(b % a, a); }
int lcm(int a, int b) { return a / gcd(a, b) * b; }

struct Coin {
	string val;
	LL divisor[9];
};

LL getDevisor(LL k) {
	for (LL i = 2; 1LL * i * i <= k; ++i) {
		if (k % i == 0) {
			return i;
		}
	}

	return 0;
}

void check(const vector<int> &num, vector<Coin> &ans) {
	Coin c;
	int ok = 0;

	FOR(i, 0, num.size()) {
		c.val += (num[i] ? '1' : '0');
	}

	FOR(base, 2, 11) {
		LL k = 0;
		LL d = 1;

		for (int i = num.size() - 1; i >= 0; --i) {
			k += num[i] * d;
			d *= base;
		}

		c.divisor[base - 2] = getDevisor(k);
		ok += c.divisor[base - 2] != 0;
	}

	if (ok == 9) {
		ans.push_back(c);
	}
}

int main() {
	init();

	int t;
	cin >> t;

	FOR(i, 1, t + 1) {
		printf("Case #%d:\n", i);

		vector<Coin> ans;

		int n, p;
		cin >> n >> p;

		vector<int> num(n, 0);
		num[0] = num[n - 1] = 1;

		FOR(j, 0, (1 << (n - 2))) {
			if (ans.size() == p) {
				break;
			}

			LL d = j;
			FOR(k, 1, n - 1) {
				num[k] = d & 1;
				d >>= 1;
			}

			check(num, ans);
		}

		FOR(j, 0, p) {
			cout << ans[j].val;
			FOR(k, 0, 9) {
				cout << " " << ans[j].divisor[k];
			}
			cout << "\n";
		}
	}

	finish();
	return 0;
}