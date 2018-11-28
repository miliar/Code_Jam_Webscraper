#include <iostream>
#include <iomanip>
using namespace std;

int T, nCase = 1;
double C, F, X;

double solve() 
{
	double prod = 2.0;
	double T = X/prod;
	double cost = 0;
	
	while (true) {
		cost += C/prod;
		prod += F;
		if ( cost + X/prod >= T )
			break;
		else
			T = cost + X/prod;
	}
	return T;
}

int main()
{
	cin >> T;
	while (T--) {
		cin >> C >> F >> X;
		cout << fixed << setprecision(7) ;
		cout << "Case #" << nCase ++ << ": " << solve() << endl;
	}
	return 0;
}