# include <iostream>
#include <string>

using namespace std;

int main(){

	int num_cases;
	cin >> num_cases;
	double farm_cost, rate_inc, target;
	cout.precision(7);
	
	for(int i = 1; i <= num_cases; i++){
		cin >> farm_cost >> rate_inc >> target;

		double rate = 2.0;
		double totaltime = 0;
		while(target/rate > farm_cost/rate + target/(rate+rate_inc)){
			totaltime += farm_cost/rate;
			rate += rate_inc;
		}

		totaltime += target/rate;
		cout << std::fixed;
		cout << "Case #" << i << ": " << totaltime << endl;
	}
	return 0;
}