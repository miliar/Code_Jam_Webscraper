// GCJ Round 2 2013
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows
bool could_win(LL k, LL p, int n)
{
	if (p >= (1LL << n))
		return true;
	if (k == (1LL << n) - 1)
		return false;
	return could_win(k - k / 2, p, n - 1);
}
bool could_not_win(LL k, LL p, int n)
{
	if (p <= 0)
		return true;
	if (p >= (1LL << n))
		return false;
	if (k == (1LL << n) - 1)
		return true;
	if (k == 0)
		return false;
	return could_not_win((k - 1) / 2, p - (1LL << (n - 1)), n - 1);
}
int main(int argc, char **argv)
{
	int kase;
	int n_read = scanf("%d\n", &kase);
	assert(n_read == 1);
	int kase_a = 0, kase_b = oo;
	if (argc > 1)
	{
		assert(argc == 3);
		int n_read = sscanf(argv[1], "%d", &kase_a);
		assert(n_read == 1);
		n_read = sscanf(argv[1], "%d", &kase_b);
		assert(n_read == 1);
		if (kase_a >= kase)
			return 0;
	}
	for (int tkase=0; tkase<kase; tkase++)
	{
		// read case
		int n;
		LL p;
		cin >> n >> p;
		LL gw = (1LL << n) - 1, cw = 0;
		LL lower = 1, upper = (1LL << n) - 1;
		while (lower <= upper)
		{
			LL mid = lower + (upper - lower) / 2;
			if (could_win(mid, p, n))
			{
				lower = mid + 1;
				cw = mid;
			}
			else
			{
				upper = mid - 1;
			}
		}
		/*
		for (int i=0; i<(1<<n); i++)
			if (could_win(i, p, n))
				cw = i;
		*/
		lower = 0, upper = (1LL << n) - 1;
		while (lower <= upper)
		{
			LL mid = lower + (upper - lower) / 2;
			if (could_not_win(mid, p, n))
			{
				upper = mid - 1;
			}
			else
			{
				lower = mid + 1;
				gw = mid;
			}
		}
		/*
		for (int i=1; i<(1<<n); i++)
			if (could_not_win(i, p, n))
			{
				gw = i - 1;
				break;
			}
		*/
		if (tkase < kase_a || tkase >= kase_b)
			continue;
		// process case
		printf("Case #%d: ", tkase+1);
		cout << gw << " " << cw << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
