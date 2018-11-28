#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int num_cases;
	cin >> num_cases; cin.ignore();


	//C = 30.0 , F = 2.0 , X = 100.0
	//the question is, is the time waiting to buy another farm + going from 0 to that farm < time to get the cookies from where we are now
	//if yes, buy the farm, if not wait and end
	double start_rate = 2.0;
	double rate = start_rate;
	double total_time = 0;

	for (int i = 1; i <= num_cases; ++i) {
		total_time = 0;
		rate = start_rate;
		double cost, farm_rate, x;
		cin >> cost >> farm_rate >> x; cin.ignore();
		
		while (true) {//go until we get the desired amount of cookies
			double waiting_time = x/rate; //how long if we don't buy the farm
			double farm_time = cost/rate + x/(rate + farm_rate);//how long if we purchase the farm
			//cout << "waiting_time: " << waiting_time << " farm_time: " << farm_time << endl;
			if (farm_time < waiting_time) {
				total_time += cost/rate;
				rate += farm_rate;
				//cout << "total_time: " << total_time << endl;
			} else {
				total_time += waiting_time;
				//cout << "total_time: " << total_time << endl;
				//cout << setprecision(7) << "Case #" << i << ": " << total_time << endl;
				printf("Case #%d: %.7f\n", i, total_time);
				break;
			}
		}
	}
}