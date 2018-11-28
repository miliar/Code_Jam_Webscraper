#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include "math.h"

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define fori(i, a, b) for (int i = int(a); i <= int(b); i++)

typedef long long ll;

using namespace std;

int n;
double v, x;
double r[100], c[100];
int ps[100];
int psn = 0;
int ns[100];
int nsn = 0;
const double EPS = 1e-8;

double f() {
	double rn = 0;
	double rp = 0;
	double cun = 0;
	double cup = 0;
	bool fz = false;
	psn = 0;
	nsn = 0;
	forn(i, n) {
		if (fabs(c[i] - x) < EPS) {
			fz = true;
		}
		if (c[i] <= x) {
			ns[nsn] = i;
			nsn++;
			rn += r[i];
			cun += c[i] * r[i];
		} else {
			ps[psn] = i;
			psn++;
			rp += r[i];
			cup += c[i] * r[i];
		}
	}
	if ((psn == 0 || nsn == 0) && !fz) {
		return -1;
	}
	double z = (cun + cup) / (rn + rp);
	if (fabs(z - x) < EPS) {
		return v / (rn + rp);
	}
	if (z > x) {
		forn(i, psn) {
			int m = i;
			fori(j, i + 1, psn - 1) {
				if (c[ps[j]] > c[ps[m]]) {
					m = j;
				}
			}
			int t = ps[i];
			ps[i] = ps[m];
			ps[m] = t;
		}
		int k;
		forn(i, psn) {
			k = ps[i];
			cup -= c[k] * r[k];
			rp -= r[k];
			z = (cun + cup) / (rn + rp);
			if (fabs(z - x) < EPS) {
				return v / (rn + rp);
			}
			if (i == psn - 1) {
				break;
			}
			if (z <= x) {
				break;
			}
		}
		double kb = 0;
		double ke = 1;
		double km;
		double rpm;
		while (true) {
			km = (kb + ke) / 2;
			rpm = rp + r[k] * km;
			double zm = (cun + cup + r[k] * km * c[k]) / (rn + rpm);
			if (fabs(zm - x) < EPS) {
				break;
			}
			if (zm < x) {
				kb = km;
			} else {
				ke = km;
			}
		}
		return v / (rn + rpm);
	} else {
		forn(i, nsn) {
			int m = i;
			fori(j, i + 1, nsn - 1) {
				if (c[ns[j]] < c[ns[m]]) {
					m = j;
				}
			}
			int t = ns[i];
			ns[i] = ns[m];
			ns[m] = t;
		}
		int k;
		forn(i, nsn) {
			k = ns[i];
			cun -= c[k] * r[k];
			rn -= r[k];
			z = (cun + cup) / (rn + rp);
			if (fabs(z - x) < EPS) {
				return v / (rn + rp);
			}
			if (i == nsn - 1) {
				break;
			}
			if (z > x) {
				break;
			}
		}
		double kb = 0;
		double ke = 1;
		double km;
		double rnm;
		while (true) {
			km = (kb + ke) / 2;
			rnm = rn + r[k] * km;
			double zm = (cun + r[k] * km * c[k] + cup) / (rnm + rp);
			if (fabs(zm - x) < EPS) {
				break;
			}
			if (zm > x) {
				kb = km;
			} else {
				ke = km;
			}
		}
		return v / (rnm + rp);
	}
}

int main() {
	int ntc;
	cin >> ntc;
	fori(tc, 1, ntc) {
		cin >> n >> v >> x;
		forn(i, n) {
			cin >> r[i] >> c[i];
		}
		cout << "Case #" << tc << ": ";
		double t = f();
		if (t < 0) {
			cout << "IMPOSSIBLE";
		} else {
			printf("%.9f", t);
		}
		cout << endl;
	}
	return 0;
}
