#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	cout.precision(7);
	for (int i = 1; i <= n; ++i){
		double current_rate = 2.0;
		double C;
		double F;
		char *output = "Case #";
		double X;
		cin >> C >> F >> X;
		double acc_time = 0.0;

		double next_rate = current_rate + F;
		
		while (X / current_rate > X / next_rate + C / current_rate) {
			acc_time += C / current_rate;
			current_rate = next_rate;
			next_rate += F;
		}

		acc_time += X / current_rate;

		cout << output << i << ": " << fixed << acc_time << endl;
	}

}