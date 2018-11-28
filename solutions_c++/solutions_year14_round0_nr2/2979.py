#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <fstream>

using namespace std;

const double F0 = 2.0;

int calc_n(double C, double F, double X) {
	int n = 0;
	double val = X / F0;

	double s1 = 0.0;
	for (int k = 1; k < X; ++k) {
		s1 += 1.0 / (F0 + F * (k - 1));

		double cur_val = C * s1 + X / (k * F + F0);
		if (cur_val < val) {
			val = cur_val;
			n = k;
		}
	}

	return n;
}

double precise_sum(set<double>& a) {
	while (a.size() >= 2) {
		double val = *(a.begin());
		a.erase(a.begin());
		val += *(a.begin());
		a.erase(a.begin());
		a.insert(val);
	}

	return *(a.begin());
}

double solve(int n, double C, double F, double X) {
	set<double> a;
	for (int k = 1; k <= n; ++k) {
		a.insert(C / (F0 + F * (k - 1)));
	}
	a.insert(X / (n * F + F0));

	return precise_sum(a);
}

int main() {
	ifstream input("B-large.in");
	ofstream output("B-large.out");

	int test_count;
	input >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		double C, F, X;
		input >> C >> F >> X;
		int n = calc_n(C, F, X);
		output << "Case #" << i << ": " << setprecision(7) << fixed << solve(n, C, F, X) << endl;
	}

	return 0;
}
