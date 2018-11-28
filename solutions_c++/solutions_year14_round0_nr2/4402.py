#include <iostream>
#include <iomanip>
using namespace std;

double C, F, X;

double t_mem[1000000];

double t(int n) {
	double res = X / (2 + n * F);
	double tmp = 0;
	for (int k = 0; k < n; k++)
		tmp += 1 / (2 + k * F);
	res += C * tmp;
	if (n == 0)
		res = X / (2 + n * F);
	else
		res = t_mem[n - 1] + C / (2 + (n-1) * F);
	t_mem[n] = res;
	return res;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		double val, best;
		int i;
		cin >> C >> F >> X;
		best = t(0);
		i = 1;
		while ((val = t(i)) < best) {
			best = val;
			i++;
		}
		cout << "Case #" << icase << ": " << fixed << setprecision(9) << best << endl;
	}
	return 0;
}
