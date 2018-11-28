#include <iostream> 
#include <iomanip>

using namespace std;

double cal_min_time(double C, double F, double X);

int main() {
	int T; // test case number
	double C, F, X;
	double total_time;

	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> C >> F >> X;
		total_time = cal_min_time(C, F, X);
		cout << "Case #" << i << ": " << fixed << setprecision(7) << total_time << endl;
	}
}

double cal_min_time(double C, double F, double X) {
	double current_seconds = 0.0;
	double current_prod = 2.0;	// current production per seconds
	double total_seconds = 0.0;

	while (true) {
		current_seconds = C/current_prod;
		// buy cookies farm
		if ((C/current_prod + X/(current_prod+F)) < X/current_prod) {
			total_seconds += current_seconds;
			current_prod += F;
		}
		else {
			break;
		}
	}
	total_seconds += X/current_prod;

	return total_seconds;
}
