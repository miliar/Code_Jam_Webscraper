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
const LL MOD = 1000002013LL;
typedef pair<LL, LL> PLL;
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
		int n, m;
		cin >> n >> m;
		map<int, PLL> events;
		LL cost2 = 0;
		for (int i=0; i<m; i++)
		{
			int begin, end;
			long long count;
			cin >> begin >> end >> count;
			assert(begin < end);
			events[begin].first += count;
			events[end].second += count;
			LL tmp = n * (n - 1);
			tmp -= (n - (end - begin)) * (n - (end - begin) - 1);
			tmp /= 2;
			tmp %= MOD;
			tmp *= count;
			tmp %= MOD;
			cost2 += tmp;
			cost2 %= MOD;
		}
		if (tkase < kase_a || tkase >= kase_b)
			continue;
		// process case
		LL cost = 0;
		int last_stop = -1;
		LL n_passengers = 0;
		map<int, LL> tickets;
		FORIT(it, events)
		{
			int current_stop = it->first;
			//cout << "@" << current_stop << endl;
			map<int, LL> next_tickets;
			if (last_stop != -1)
			{
				LL dist = current_stop - last_stop;
				FORIT(jt, tickets)
				{
					LL tmp = jt->first * (jt->first - 1);
					tmp -= (jt->first - dist) * (jt->first - dist - 1);
					tmp /= 2;
					tmp %= MOD;
					tmp *= jt->second;
					tmp %= MOD;
					cost += tmp;
					cost %= MOD;
					next_tickets[jt->first - dist] += jt->second;
				}
			}
			next_tickets[n] += it->second.first;
			n_passengers += it->second.first;
			n_passengers -= it->second.second;
			assert(n_passengers >= 0);
			tickets.clear();
			LL n_passengers2 = n_passengers;
			//COUT(n_passengers2);
			FORIT(jt, next_tickets)
			{
				LL n_keep = min(n_passengers2, jt->second);
				n_passengers2 -= n_keep;
				if (n_keep > 0)
				{
					tickets[jt->first] += n_keep;
					//cout << "keeping " << n_keep << " " << jt->first << endl;
				}
			}
			last_stop = current_stop;
		}
		printf("Case #%d: ", tkase+1);
		LL cost_diff = cost2 - cost;
		cost_diff %= MOD;
		cost_diff += MOD;
		cost_diff %= MOD;
		//cout << cost << " " << cost2 << endl;
		cout << cost_diff << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
