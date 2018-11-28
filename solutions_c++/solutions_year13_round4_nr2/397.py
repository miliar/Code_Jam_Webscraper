#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;
typedef long double ld;

ll N, P;

string conv(ll P) {
	P--;
	string status = "";
	for (int i = 0; i < N; ++i) {
		status += (P & 1 ? "1" : "0");
		P >>= 1;
	}
	reverse(status.begin(), status.end());
	return status;
}

string mustWin(ll cur, ll stronger) {
	string res = "";
	for (int i = 0; i < N; ++i) {
		if (stronger > 0) {
			res += "1";
			stronger--;
			stronger /= 2;
		} else {
			res += "0";
		}
	}
	return res;
}

string canWin(ll cur, ll weaker) {
	string res = "";
	for (int i = 0; i < N; ++i) {
		if (weaker > 0) {
			res += "0";
			weaker--;
			weaker /= 2;
		} else {
			res += "1";
		}
	}
	return res;
}

ll calc1() {
	string target = conv(P);
	ll lo = 0, hi = (1ll << N)-1;
	while (lo < hi) {
		ll mid = lo + (hi - lo + 1) / 2;
		if (mustWin(mid, mid) <= target)
			lo = mid;
		else
			hi = mid - 1;
	}
	return lo;
}

ll calc2() {
	string target = conv(P);
	ll lo = 0, hi = (1ll << N)-1;
	while (lo < hi) {
		ll mid = lo + (hi - lo + 1) / 2;
		if (canWin(mid, (1ll << N) - 1 - mid) <= target)
			lo = mid;
		else
			hi = mid - 1;
	}
	return lo;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("1.in", "rt", stdin);
//	freopen("1A/C-small-1-attempt0.in", "rt", stdin);
//	freopen("1A/C-small-1.out","wt",stdout);
//	freopen("1A/C-small-2-attempt5.in", "rt", stdin);
//	freopen("1A/C-small-2-attempt5.out", "wt", stdout);
//	freopen("2/B-small-attempt1.in", "rt", stdin);
//	freopen("2/B-small-attempt1.out","wt",stdout);
	freopen("2/B-large.in", "rt", stdin);
	freopen("2/B-large.out","wt",stdout);
#endif
	int n;
	cin >> n;
	for (int tt = 0; tt < n; ++tt) {
		cout << "Case #" << tt + 1 << ": ";
		cin >> N >> P;

//		cout << conv(P) << " " << conv(P - 1) << endl;
//		for (int i = 0; i < 1 << N; ++i) {
//			cout << i << " " << mustWin(i, i) << " "
//					<< canWin(i, (1 << N) - 1 - i) << endl;
//		}
		cout << calc1() << " " << calc2() << endl;
	}
	return 0;
}
