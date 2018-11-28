#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define range(i,a,b) for(auto i=(a);i<(b);i++)
#define rep(i,n) range(i,0,n)
#define all(c) begin(c),end(c)
#define CLR(i,x) memset(i,x,sizeof(i))
#define clr0(i) CLR(i,0)
#define clr1(i) CLR(i,-1)
#define bit(x,i) ((x>>i)&1)
#define M(x) ((x)%MOD)
#define acc(f,x,y) x=f(x,y)
#define fst first
#define snd second
#define tup make_tuple

double work() {
	int n, k;
	scanf("%d%d", &n, &k);

	vd ps;
	rep(i, n) {
		double x;
		scanf("%lf", &x);
		ps.push_back(x);
	}

	double ans = -1;

	rep(s, 1<<n)
	if(__builtin_popcount(s) == k) {
		double sp = 0;
		for(int t = s; t; t = (t - 1) & s)
		if(__builtin_popcount(t) == k / 2) {
			double tp = 1;
			rep(i, n) if((s >> i) & 1) {
				if((t >> i) & 1)
					tp *= ps[i];
				else
					tp *= 1 - ps[i];
			}
			sp += tp;
		}
		acc(max, ans, sp);
	}

	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	rep(i, t) {
		printf("Case #%d: %.7lf\n", i + 1, work());
	}
	return 0;
}
