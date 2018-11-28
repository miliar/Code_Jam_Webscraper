#include <iostream>
using namespace std;

inline double min(const double& a, const double& b)
{
	return a < b ? a : b;
}

double calc(double C, double F, double X, double step, double money)
{
	if (C >= X) {
		return X / step;
	}
	if (money >= X) {
		return 0;
	}
	
		double t = (C - money) / step;
		double t1 = (X - C) / step;
		double t2 = X / (step + F);
		// cout << t << ' ' << t1 << ' ' << t2 << endl;
		if (t1 < t2) {
			return X / step;
		}
		return t + calc(C, F, X, step + F, 0);
	


}

int main() 
{
	freopen("b.txt", "r", stdin);
	freopen("b.output", "w", stdout);
	int T;
	double C, F, X;
	int a[4][4], b[4][4];

	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> C >> F >> X;
		cout.precision(7);
		printf("Case #%d: %.7lf\n", i +1 ,calc(C, F, X, 2, 0));
		//cout << "Case #" << i + 1 << ": " << calc(C, F, X, 2, 0) << endl;
		
	}



	return 0;
}