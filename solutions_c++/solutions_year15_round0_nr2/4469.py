#define _USE_MATH_DEFINES

#include <algorithm>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define SREP(s,i,n) for(int i=s;i<(int)(n);++i)
#define REP(i,a) SREP(0,i,a)
#define ALL(a) (a).begin(),(a).end()

#define CLR(a) memset(a,0,sizeof(a))
#define REMOVE_AT(v,i) v.erase(v.begin()+i)

using namespace std;
const double EPS = 1e-8;
const double D_INF = 1e12;
const int I_INF = 1 << 29;
typedef long long LL;

int D;
vector<int> P;

int solve() {
	int res;
	int m = -1;
	int ind = -1;
	REP(i, P.size()) {
		if (m < P[i]) {
			m = P[i];
			ind = i;
		}
	}
	res = m;
	int cur = m;
	m = sqrt(m) + 1;
	P.erase(P.begin() + ind);
	for (int i = 2; i <= m; i++) {
		int cnt = cur / i + (cur % i ? 1 : 0);
		if (cnt <= 1) {
			continue;
		}
		int rest = cur;
		REP(j, i-1) {
			P.push_back(cnt);
			rest -= cnt;
		}
		P.push_back(rest);
		res = min(res, i - 1 + solve());
		REP(j, i) {
			P.pop_back();
		}
	}
	P.insert(P.begin() + ind, cur);
	//cout << res << endl;
	return res;
}

int main(){
	int T;
	cin >> T;
	REP(tc, T) {
		cin >> D;
		P.clear();
		REP(i, D) {
			int pp;
			cin >> pp;
			P.push_back(pp);
		}
		cout << "Case #" << (tc + 1) << ": ";
		cout << solve() << endl;
	}
	return 0;
}