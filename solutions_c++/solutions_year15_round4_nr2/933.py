#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <math.h>
#include <cassert>
#include <cxxptl.h>
#include <sys/time.h>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

typedef pair<double, double> PDD;

double V, X;
vector<pair<double, double> > sLess, sExact, sMore; // (rate, temperature)
vector<PDD> sAll;

double can()
{
	double maxT = 1;
	double sV = 0;
	REP(i, sAll) sV += maxT * sAll[i].first;
	double sCV = 0;
	REP(i, sAll) sCV += maxT * sAll[i].first * sAll[i].second;
	if (sCV / sV > X) {
		// mixture too hot:
		REP(i, sMore) {
			double Ri = sMore[i].first;
			double Ci = sMore[i].second;
			if ((sCV - maxT * Ri * Ci) / (sV - maxT * Ri) < X) {
				double p = (X * sV - sCV) / (X * Ri - Ri * Ci);
				assert(p >= -1e-9);
				assert(p <= maxT+1e-9);
				sCV -= p * Ri * Ci;
				sV -= p * Ri;
			} else {
				sCV -= maxT * Ri * Ci;
				sV  -= maxT * Ri;
			}
		}
	} else {
		REP(i, sLess) {
			double Ri = sLess[i].first;
			double Ci = sLess[i].second;
			if ((sCV - maxT * Ri * Ci) / (sV - maxT * Ri) > X) {
				double p = (X * sV - sCV) / (X * Ri - Ri * Ci);
				assert(p >= -1e-9);
				assert(p <= maxT+1e-9);
				sCV -= p * Ri * Ci;
				sV -= p * Ri;
			} else {
				sCV -= maxT * Ri * Ci;
				sV  -= maxT * Ri;
			}
		}
	}
	double endT = sCV / sV;
	assert(fabs(endT - X) < 1e-4);
	return V / sV;
}

double solve(void)
{
	sLess.clear();
	sExact.clear();
	sMore.clear();
	sAll.clear();
	int n;
	scanf("%d%lf%lf", &n, &V, &X);
	FOR(i, n) {
		pair<double, double> value;
		scanf("%lf%lf", &value.first, &value.second);
		sAll.push_back(value);
		if (value.second == X) sExact.push_back(value);
		else if (value.second < X) sLess.push_back(value);
		else sMore.push_back(value);
	}
	sort(sLess.begin(), sLess.end(), [](const PDD& left, const PDD& right) { return left.second < right.second; });
	sort(sMore.begin(), sMore.end(), [](const PDD& left, const PDD& right) { return left.second > right.second; });
	
	if (sExact.empty() && (sLess.empty() || sMore.empty())) return -1;
	if (sLess.empty() || sMore.empty()) {
		double sRate = 0;
		REP(i, sExact) sRate += sExact[i].first;
		return V / sRate;
	}
	
	return can();
}

int main(int argc, char** argv)
{
#ifdef __LOCAL__
	freopen("/home/vesko/gcj/b.in", "rt", stdin);
#endif
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		double res = solve();
		if (res >= 0)
			printf("Case #%d: %.7lf\n", tc, res );
		else {
			printf("Case #%d: IMPOSSIBLE\n", tc);
/*			printf("V = %.9lf, tC = %.9lf\n", V, X);
			REP(i, sAll) printf("%.9lf, %.9lf\n", sAll[i].first, sAll[i].second);*/
		}
	}
	return 0;
}
