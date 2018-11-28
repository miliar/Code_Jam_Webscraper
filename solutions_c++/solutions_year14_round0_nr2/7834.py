#include<iostream>
#include<iomanip>
using namespace std;


double C, F, X;
int main(){
	int testcases;
	cin >> testcases;
	
	for (int test_i = 1; test_i <= testcases; ++test_i){
		cin >> C >> F >> X;

		int cookie_farm_cnt = 0;

		double answer = X / 2.0;
		double cookie_rate = 2.0;

		double time_to_build_farms = 0.0;
		while (++cookie_farm_cnt){
			time_to_build_farms += (C / cookie_rate);
			cookie_rate += F;

			double time_to_end = time_to_build_farms + (X / cookie_rate);
			if (answer > time_to_end)
				answer = time_to_end;
			else break;
		}
		cout << "Case #" << test_i << ": " << setiosflags(ios::fixed) << setprecision(7) << answer << "\n";
	}
	return 0;
}