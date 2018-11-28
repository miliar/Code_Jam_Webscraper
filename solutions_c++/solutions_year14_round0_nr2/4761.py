#include <iostream>
#include <iomanip>
#include <cstdio>


using namespace std;

int T;
double C, F, X;
double doSolve() {
	double time = 0.0f;
	cin >> C;
	cin >> F;
	cin >> X;
	double remaining = X;
	double present_rate = 2;
	double farm_val = C;
	while(1) {	
		//cout << "remaining: " << remaining << " present_rate: " << present_rate << " time: " << time << endl;
		if (remaining <= farm_val) {
			time += (remaining / present_rate); 
			break;
		} else {
			// calculate till the farm value is reached
			double temp_time = farm_val / present_rate;
			double time_if_sold = (remaining) / (present_rate + F);
			double time_if_not_sold = (remaining - farm_val) / (present_rate);
			//cout << "temp_time: " << temp_time << " if sold: " << time_if_sold << " if not: " << time_if_not_sold << endl;
			time += temp_time;
			if (time_if_sold < time_if_not_sold) {
				present_rate += F;
			} else {
				remaining = remaining - farm_val;
			}
		}
	}
	return time;
}
int main() {
	cin >> T;
	for (int i = 1 ; i <= T ; i++) {
		double val = doSolve();
//		cout << "Case #" << i << ": " << std::setprecision(7) << val << endl;
		printf("Case #%d: %.7f\n", i, val);
	}

}
