#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()
#define INF 1001001001

string i2s(int x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
int s2i(string s) { istringstream i(s);  int x;  i >> x;  return x; }

long long n, k;

int best(long long x) {
	int res = 0;
	int bestpos = (1LL << n);
	long long weaker = (1LL << n) - 1 - x;
	FOR(round, 1, n) { //to win round i need to have 2^i-1 weaker team
		long long need = (1 << round) - 1;
		if (weaker >= need) {
			res = round;
			bestpos /= 2;
		}
	}
	return bestpos - 1;
}

int worst(long long x) {
	int res = 0;
	int worstpos = 0;
	long long stronger = x;
	FOR(round, 1, n) { //to lost round i need to have 2^i-1 weaker team
		long long need = (1LL << round) - 1;
		if (stronger >= need) {
			res = round;
			worstpos += (1LL << (n - round));
		}
	}
	return worstpos;
}

long long process1() {
	long long res = -1;
	long long left = 0;
	long long right = (1LL << n) - 1;
	while (left <= right) {
		long long mid = (left + right) / 2;
		if (worst(mid) < k) {
			res = mid;
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	return res;
}

long long process2() {
	long long res = -1;
	long long left = 0;
	long long right = (1LL << n) - 1;
	while (left <= right) {
		long long mid = (left + right) / 2;
		if (best(mid) < k) {
			res = mid;
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	return res;
}




int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int test;
	cin >> test;
	REP(itest,test) {
		cin >> n >> k;
		//REP(i, (1LL << n)) cout << worst(i) << endl;
		cout << "Case #" << itest+1 << ": " << process1() << " " << process2() << endl;
	}
	return 0;
}
