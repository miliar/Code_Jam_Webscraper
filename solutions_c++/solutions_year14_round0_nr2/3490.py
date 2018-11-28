#include <fstream>
#include <cstdio>

using namespace std;

ifstream in("cinput.txt");
ofstream out("coutput.txt");

double solve(double c, double f, double x) {
	double best = x/2;
	int nf = 0;
	double cps = 2;
	double cto = 0;

	while (cto < best) {
		++nf;
		cto += c/cps;
		cps = 2 + (nf*f);

		if (cto + (x/cps) < best)
			best = cto + (x/cps);
	}

	return best;
}

int main() {
	int t;
	in >> t;
	out.precision(8);

	for (int i = 1; i <= t; ++i) {
		double c, f, x;
		in >> c >> f >> x;

		out << "Case #" << i << ": " << solve(c, f, x) << "\n";
	}

	return 0;
}

