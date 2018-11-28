#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <map>
#include <set>
using namespace std;

typedef long long		ll;
typedef pair<int, int> 	ii;
typedef vector<ii>		vii;
typedef vector<int>		vi;
typedef set<int>		si;
typedef map<string, int>msi;

#define INF 1000000000
#define REP(i, n) \
	for (int i = 0; i < int(n); i++) //i is local
#define TRvi(c, it) \
	for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
	for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
	for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back

double minTime(double C, double F, double X, double hargaMati, double hargaTotal, double jumlahFarm) {
	double hargaMati2 = hargaMati + C / (2.0+jumlahFarm*F);
	double hargaTotal2 = hargaMati2 + (X-jumlahFarm*C) / (2.0+jumlahFarm*F);
	if (hargaTotal2 > hargaTotal) {
		return hargaTotal;
	} else {
		return minTime(C, F, X, hargaMati2, hargaTotal2, jumlahFarm+1);
	}
}

double minTime(double C, double F, double X) {
	double time = 0;
	double rate = 2.0;
	double wait = 0.0;
	double buy = 0.0;
	while (true) {
		wait = X / rate;
		buy = C / rate + X / (rate + F);
		if (wait <= buy) {
			return time + wait;
		} else {
			time += C / rate;
			rate += F;
		}
	}
}

int main() {
	int T;
	int nCase = 1;
	scanf("%d ", &T);
	while(T--) {
		double fAns = 0;
		double C, F, X;
		scanf("%lf %lf %lf ", &C, &F, &X);
		fAns = minTime(C, F, X);
		printf("Case #%d: %.7lf\n", nCase++, fAns);
	}
	return 0;
}