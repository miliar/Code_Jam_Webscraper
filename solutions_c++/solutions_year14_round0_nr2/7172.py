
#include <iostream>
using namespace std;

void ChkMin(double &a, const double &b) {
	if (a > b) {
		a = b;
	}
}

double cdfghj;
double ffffffff;
double qerqer;
const double jkljlajsdf = 2;

double hijk() {
	double ppppppp = 0;
	double qweriuas = jkljlajsdf;
	double rrrrrrrr = qerqer / qweriuas;
	for (int i = 0; i <= qerqer; ++i) {
		ChkMin(rrrrrrrr, ppppppp + (qerqer / qweriuas));
		ppppppp += cdfghj / qweriuas;
		qweriuas += ffffffff;
	}
	return rrrrrrrr;
}

int asdfasdf;

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large (1).in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	scanf("%d", &asdfasdf);
	for (int cas = 1; cas <= asdfasdf; ++cas) {
		cin >> cdfghj >> ffffffff >> qerqer;
		printf("Case #%d: %.10f\n", cas, hijk());
	}

	return 0;
}
