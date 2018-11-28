#include<windows.h>
#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<iomanip>

int main(int argc, char* argv[]){
	

	std::string input = "", holder = "";
	char test = ',';
	int test_cases = 0, test_case_on = 0, cookies = 0, counter = 0, num_of_farms = 0;
	double cost = 0, rate = 2, goal = 0, farm_rate = 0, total  = 0, seconds_till_farm = 0, max_seconds = 0, min_seconds = 0, previous_seconds = 0, cumulative_seconds = 0, seconds_till_goal = 0, inital_ratio = 0, new_ratio = 0;
	bool answer_found = false;
	std::getline(std::cin, input);
	test_cases = std::stoi(input);
	while (test_cases != test_case_on){
		std::getline(std::cin, input);
		cumulative_seconds = 0;
		input += ' ';
		holder = "";
		num_of_farms = 0;
		counter = 0;
		answer_found = false;
		rate = 2;
		while (counter != input.length()){
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			cost = atof(holder.c_str());
			test = ',';
			holder = "";
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			farm_rate = atof(holder.c_str());
			test = ',';
			holder = "";
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			goal = atof(holder.c_str());
		}
		max_seconds = goal / rate;
		previous_seconds = max_seconds;
		if (max_seconds <= 1){
			min_seconds = max_seconds;
			answer_found = true;
		}
		while (!answer_found){
			seconds_till_farm = cost / rate;
			rate += farm_rate;
			seconds_till_goal = goal / rate;
			total = (cumulative_seconds + seconds_till_farm + seconds_till_goal);
			if (total < previous_seconds){
				previous_seconds = total;
			}
			else if (total > previous_seconds){
				min_seconds = previous_seconds;
				break;
			}
			cumulative_seconds += seconds_till_farm;
		}
		std::cout << std::fixed;
		std::cout << "Case #" + std::to_string(test_case_on + 1) + ": " << std::setprecision(7) << min_seconds << '\n';
		test_case_on++;
	}
	return 0;
}