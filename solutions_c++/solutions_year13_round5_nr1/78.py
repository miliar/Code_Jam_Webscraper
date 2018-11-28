#include <deque>
#include <queue>
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
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------

double get_profit(vector<LL> v, vector<LL> u) {
	LL mi = 1LL << 62;
	int num = 0;
	rep(i, 0, sz(v)) {
		if(u[i] + v[i] < mi) {
			mi = u[i]+v[i];
			num = 1;
		} else if(u[i]+v[i] == mi) {
			num++;
		}
	}
	double ret = 0.0;
	rep(i, 0, sz(v)) {
		if(u[i]+v[i] == mi) {
			ret += u[i]*36 / (double)num;
		}
	}
	rep(i, 0, sz(u)) ret -= u[i];
	return ret;
}


LL need(vector<LL> v, int num, LL x) { // x >= max(v[0]...v[num-1])
	LL ret = 0;
	rep(i, 0, num) {
		ret += (x-v[i]);
	}
	rep(i, num, sz(v)) {
		if(v[i] <= x) {
			ret += (x+1 - v[i]);
		}
	}
	return ret;
}

LL findX(vector<LL> v, int num, LL B) {
	LL lo = 0, hi = 1LL << 50;
	rep(i, 0, num) lo = max(lo, v[i]);
	if(need(v, num, lo) > B) return -1;
	while(lo+1 < hi) {
		LL mid = (lo + hi)/2;
		if(need(v, num, mid) <= B) {
			lo = mid;
		} else {
			hi = mid;
		}
	}
	return lo;
}

int main() {
	freopen("F:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-large.out", "w", stdout);

	int T;
	cin>>T;
	rep(te, 1, T+1) {
		LL B;
		int N;
		cin>>B>>N;

		vector<LL> v;
		rep(i, 0, N) {
			LL x; cin>>x;
			v.push_back(x);
		}
		rep(i, sz(v), 37) v.push_back(0);
		sort(all(v));
		
		double ans = 0.0;
		rep(num, 1, 37) {
			LL x = findX(v, num, B);
			vector<LL> u(37, 0);
			rep(i, 0, num) {
				u[i] = x-v[i];
			}
			rep(i, num, 37) {
				if(v[i] <= x) {
					u[i] = x+1 - v[i];
				}
			}
			ans = max(ans, get_profit(v, u));
		}

		printf("Case #%d:", te);
		printf(" %.10lf\n", ans);
	}
}

