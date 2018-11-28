#include <math.h>
#include <iostream>
#include <iomanip>
using namespace std;

double C, F, X;
int t;

int main()
{
	cin >> t;
	for (int i = 1; i <= t; i++){
		cin >> C >> F >> X;
		double goTime = 1, potTime = 0, delta = 2.0, sum = 0.0;
		while (1){
			goTime = X / delta;
			potTime = C / delta + X / (delta + F);
			if (goTime<potTime){
				sum += X / delta;
				break;

			}
			sum += C / delta;
			delta += F;
		}
		cout << setprecision(7) << fixed;
		cout << "Case #" << i << ": " << sum << endl;
	}
}