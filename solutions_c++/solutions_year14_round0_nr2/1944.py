#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double X,F, C;
	int cases = 0, T, N;
	cin >> T;
	while(T--) {
		double total = 0.0;
		cin >> C >> F >> X;
		N = lround(floor((X* F - 2 *C) / (F*C)));
		double s = 2.0;
		for (int i = 0;i < N; i++) {
			total += C/s;
			s += F;
		}
		total += X/s;
		cout.precision(7);
		cout << fixed<< "Case #" << ++cases << ": " << total << endl;
	}
}