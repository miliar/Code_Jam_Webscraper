#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-10;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

struct TData
{
	double r, c;
} a[1000];
double V, X;
int n;

	int isOK(double T) {
		double tV = 0, tC = 0;
		for (int i = 0; i < n; ++i) {
			double cV;
			int fg = 1;
			if (tV + a[i].r * T - V > -eps) {
				cV = V - tV;
				fg = 0;
			} else cV = a[i].r * T;
			tC = (tV * tC + cV * a[i].c) / (tV + cV);
			tV += cV;
			if (!fg) break;
		}
		double mnC = tC;
		tV = 0, tC = 0;
		for (int i = n - 1; i >= 0; --i) {
			double cV;
			int fg = 1;
			if (tV + a[i].r * T - V > -eps) {
				cV = V - tV;
				fg = 0;
			} else cV = a[i].r * T;
			tC = (tV * tC + cV * a[i].c) / (tV + cV);
			tV += cV;
			if (!fg) break;
		}
		double mxC = tC;
		return (X - mnC > -eps  && X - mxC < eps);
	}

	int cmpa(TData u, TData v) {
		return u.c < v.c;
	}

int main()
{
	int tts = 0, Tests;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%d%lf%lf", &n, &V, &X);
		double L = 0, R = 1e10;
		for (int i = 0; i < n; ++i) {
			scanf("%lf%lf", &a[i].r, &a[i].c);
			L += a[i].r;
		}
		L = V / L;
		R = max(V / a[0].r, V / a[n - 1].r);

		sort(a, a + n, cmpa);

		for (; R - L > 1E-7; ) {
			double M = (L + R) / 2;
			if (isOK(M)) R = M; else L = M;
		}

		printf("Case #%d: ", ++tts);
		if (X > a[n - 1].c || X < a[0].c) puts("IMPOSSIBLE"); else printf("%.8lf\n", R);
	}
}