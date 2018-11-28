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

void markUsed(LL num, vector<int> &cnt) {
	while (num) {
		cnt[num % 10] = 1;
		num /= 10;
	}
}

bool allChecked(const vector<int> &cnt) {
	bool ok = true;
	FOR(i, 0, 10) {
		ok &= cnt[i];
	}
	return ok;
}

int main() {
	init();

	int t;
	cin >> t;

	FOR(i, 1, t + 1) {
		int n;
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}

		vector<int> cnt(10, 0);
		LL num;
		int d = 0;

		while (!allChecked(cnt)) {
			num = n * (++d);
			markUsed(num, cnt);
		}

		printf("Case #%d: %lld\n", i, num);
	}

	finish();
	return 0;
}