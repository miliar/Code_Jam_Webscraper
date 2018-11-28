#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define pr(x) cout << #x << " = " << (x) << endl
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()

#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
const int INF = 1001001001;
const llint INFll = 9008007006005004003ll;

typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

bool equals(double a, double b) {
	if (a < b) return (b - a) < 1e-10;
	else return (a - b) < 1e-10;
}

int main() {
	int Test = in();
	for (int test = 1; test <= Test; test++) {
		int N = in();
		if (N > 2) continue;
		double V, X;
		scanf("%lf %lf", &V, &X);
		double ans = 0;
		if (N == 1) {
			double R, C;
			scanf("%lf %lf", &R, &C);
			if (! equals(C, X)) ans = -1;
			else ans = V / R;
		}
		else {
			double R1, R2, C1, C2;
			scanf("%lf %lf %lf %lf", &R1, &C1, &R2, &C2);
			if (equals(C1, X) || equals(C2, X)) {
				double R = 0;
				if (equals(C1, X)) R += R1;
				if (equals(C2, X)) R += R2;
				ans = V / R;
			}
			else {
				if ((C1 - X) * (C2 - X) > 0) ans = -1;
				else {
					if (C1 > X) swap(C1, C2), swap(R1, R2);
					double V2 = X - C1;
					double V1 = C2 - X;
					double sum = V1 + V2;
					V1 = V1 * V / sum;
					V2 = V2 * V / sum;
					ans = max(V1 / R1, V2 / R2);
				}
			}
		}
		printf("Case #%d: ", test);
		if (ans >= 0) printf("%f\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
