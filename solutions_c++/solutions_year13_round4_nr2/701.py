#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <cmath>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back
#define F first
#define S second
#define X real()
#define Y imag()

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<double> point;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

ll rank_bad(ll N, ll enemies) {
	if (enemies <= 0) return 0;
	return (1LL<<(N-1)) + rank_bad(N-1, min((enemies-1)/2, (1LL<<(N-1))-1));
}

ll rank_good(ll N, ll me) {
	if (me+1 == (1LL<<N)) return me;
	return rank_good(N-1, (me+1)/2);
}

int main() {
	int tc;
	cin >> tc;
	FOR(l, 1, tc+1) {
		ll N, P;
		cin >> N >> P;
		ll anyway_winner = -1;
		{
			ll mn = 0, mx = (1LL<<N)-1;
			while (mn < mx) {
				ll mid = (mn+mx+1)/2;
				if (rank_bad(N, mid) >= P)
					mx = mid-1;
				else
					mn = mid;
			}
			anyway_winner = mn;
		}
		ll good_winner = -1;
		{
			ll mn = 0, mx = (1LL<<N)-1;
			while (mn < mx) {
				ll mid = (mn+mx+1)/2;
				if (rank_good(N, mid) >= P)
					mx = mid-1;
				else
					mn = mid;
			}
			good_winner = mn;
		}
		cout << "Case #" << l << ": " << anyway_winner << " " << good_winner << endl;
	}
	return 0;
}

