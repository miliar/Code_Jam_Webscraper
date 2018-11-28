#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;

#define rep(a, b, e) for(int a = (int) b; a < (int) e; ++a)
#define clr(a, val) memset(a, val, sizeof(a))
#define debug(a) cerr << #a << ": " << a << endl;
#define debugv(b, t) cerr << #b << ":\n"; rep(countvec, 0, t) { cerr << b[countvec] << '\t'; } cerr << endl;
#define debugm(c, t, u) cerr << #c << ":\n"; rep(countmat, 0, t) { rep(countbb, 0, u) { cerr << c[countmat][countbb] << '\t'; } cerr << endl; }
string tos(int a) { ostringstream os(""); os << a; return os.str(); }
#define SIZE(x) int((x).size())

typedef long double ld;

int T;
double C, F, X;

void solve(int tc) {
	scanf("%lf%lf%lf", &C, &F, &X);
	double pre = 2;
	double mini = X / pre, sum = 0.0;
	int fi = 1e7;
	rep(i, 0, fi) {
		sum += C / pre;
		mini = min(mini, X / (pre + F) + sum);
		pre += F;
	}
	printf("Case #%d: %.7f\n", tc, mini);
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("D:/in.txt","r",stdin);
		freopen("D:/out.txt","w",stdout);
		clock_t start = clock();
	#endif
	
	scanf("%d", &T);
	rep(tc, 1, T + 1)
		solve(tc);
	
	#ifndef ONLINE_JUDGE
		fprintf(stderr, "\ntime=%.3lfsec\n", 0.001 * (clock() - start));
	#endif 
	return 0;
}
