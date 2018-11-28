#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <ctime>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define abs(a) ((a)<0?-(a):(a))
#define sqr(a) ((a)*(a))

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;


const long double eps = 1e-11;
const int mod = (int)1e+9 + 7;
const long double pi = acos(-1.);
const int maxn = 100100;

pair<long double, long double> pa[maxn];
int n;
long double v, x;

bool check(long double m) {
	{
		long double V = 0., X = 0.;
		for(int i = 0; i < n; i++) {
			long double sz;
			if(v - V - eps < pa[i].sc * m) {
				sz = v - V;
			} else {
				sz = pa[i].sc * m;
			}
			X = (V * X + sz * pa[i].fs) / (V + sz);
			V += sz;
		}
		if(X - eps > x) {
			return(0);
		}
	}
	{
		long double V = 0., X = 0.;
		for(int i = n - 1; i >= 0; i--) {
			long double sz;
			if(v - V - eps < pa[i].sc * m) {
				sz = v - V;
			} else {
				sz = pa[i].sc * m;
			}
			X = (V * X + sz * pa[i].fs) / (V + sz);
			V += sz;
		}
		if(X + eps < x) {
			return(0);
		}
	}
	return(1);
}

int main() {

	#ifdef SOL
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
	#else
	srand(time(0));
	const string file = "";
	if(!file.empty()) {
		freopen((file + ".in").c_str(),"r",stdin);
		freopen((file + ".out").c_str(),"w",stdout);
	}
	#endif

	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++) {
		printf("Case #%d: ", T);
		long double ob = 0;
		bool ok1 = 0, ok2 = 0;;
		double v1, x1;
		scanf("%d%lf%lf", &n, &v1, &x1);
		v = v1, x = x1;
		for(int i = 0; i < n; i++) {
			double d1, d2;
			scanf("%lf%lf", &d1, &d2);
			pa[i].sc = d1;
			pa[i].fs = d2;
			if(pa[i].fs + eps >= x) {ok1 = 1;}
			if(pa[i].fs - eps <= x) {ok2 = 1;}
			ob += pa[i].sc;
		}
		if(!ok1 || !ok2) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		sort(&pa[0], &pa[n]);
		long double l = v / ob - eps, r = (mod * 1. * mod);
		while(l + eps < r) {
			long double m = (l + r) / 2.;
			if(check(m)) {
				r = m;
			} else {
				l = m;
			}
		}
//		if(r > 1e15) {
//			printf("IMPOSSIBLE\n");
//		} else {
			printf("%.10lf\n", (double)r);
//		}
	}

	return(0);
}

// by Kim Andrey
