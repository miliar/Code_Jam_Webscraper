#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <ctime>
#include <vector>
#include <fstream>

int main()
{
	using namespace std;
	int delay;
	time_t start_time = time(NULL);
	time_t end_time;



	int cases;
	double cost, rate_farm, goal, time;
	double rate_current, time_current;
	ifstream input("input.in");
	ofstream output("output.txt");
	output.precision(14);
	
	input >> cases;
	for (int i=0; i<cases; ++i) {
		input >> cost;
		input >> rate_farm;
		input >> goal;

		rate_current = 2.0;
		time = goal / rate_current;

		for (int j=0; true; ++j) {
			rate_current = 2.0;
			time_current = 0.0;

			for (int farm_num=0; farm_num<j; ++farm_num) {
				time_current += cost/rate_current;
				rate_current += rate_farm;
			}
			time_current += goal/rate_current;

			if (time_current > time) {
				break;
			} else {
				time = time_current;
			}
		}

		output << "Case #" << i+1 << ": ";
		output << time << endl;
	}



	//end_time = time(NULL);
	//std::cout << "Ran for " << difftime(end_time, start_time) << " seconds." << endl;
	//std::cin >> delay;
	return 0;
}
