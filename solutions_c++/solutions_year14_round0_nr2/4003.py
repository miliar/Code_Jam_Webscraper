#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

int main(){
	int tests;
	cin >> tests;

	for(int i = 0; i < tests; ++i){
		double rate = 2;
		double x = 2000;
		double f = 4;
		double c = 500;

		scanf("%lf %lf %lf", &c, &f, &x);

		double add_time = 0.0;

		double result;

		while(true){
			double by_clicking = x/rate;
			double atime = c/rate;

			double by_buying = c/rate + x/(rate += f);

			if(by_clicking < by_buying){
				result = add_time + by_clicking;
				break;
			}

			add_time += atime;
		}
		
		cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(7) << result << endl;
	}
}