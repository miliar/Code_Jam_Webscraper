#include <iostream>
#include <iomanip>
using namespace std;
int main(void)
{
	int t;
	cin >> t;
	int k;
	for (k = 1; k <= t; k++) {
		double C, F, X;
		cin >> C >> F >> X;

		int counter = 0;
		double P = 2.0;
		while (((C / P + X / (P + F) ) - (float)(X / P) )< 0) {
			counter++;
			P += F;
		}
		double cost = 0;
		int i;
		for (i = counter; i > 0; i--) 
			cost += C / (F * ( counter - i) + 2);
		cost += X / P;
	cout << "Case #" << k << ": " << fixed << setprecision(7) << cost << endl;
	}
	return 0;
}
