#include<iostream>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<utility>
#include<cstring>
#include<queue>
#include<stack>
#include<climits>
using namespace std;

#define rrepp(i, from, to) for (int i = (from); i <= (to); ++i)
#define rrep(i, from, to) for (int i = (from); i < (to); ++i)
#define repp(i, from, to) for (i = (from); i <= (to); ++i)
#define rep(i, from, to) for (i = (from); i < (to); ++i)


int main()
{
	int t;
	scanf("%d", &t);
	rrepp (i, 1, t) {
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double result = 0;
		double cps = 2;
		while (c*(cps + f) < f*x) {
			result += c / cps;
			cps += f;
		}
		result += x / cps;
		printf("Case #%d: %.8f\n", i, result);
	}
	return 0;
}