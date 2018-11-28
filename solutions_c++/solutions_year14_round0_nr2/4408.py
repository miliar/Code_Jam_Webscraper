#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int caseNo = 1;
double C, F, X;

double f(int k) {
	double total = double();
	for (int i = 0; i <= k - 2; ++i)
		total += C / (double(2) + i * F);
	total += X / (double(2) + double(k - 1) * F);
	return total;
}

int main() {
	ios_base::sync_with_stdio(false);
	cout.precision(7);
	int T;
	cin >> T;
	while (T--) {
		cin >> C >> F >> X;
		cout << "Case #" << caseNo++ << ": ";
		cout << fixed << f(max(int(1 + floor(X / C - double(2) / F)), 1)) << endl;
	}
	return 0;
}