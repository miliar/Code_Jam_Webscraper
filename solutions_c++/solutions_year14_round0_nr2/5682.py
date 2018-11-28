#include<iostream>
#include<iomanip>
#include<fstream>
#include<set>
#include<map>
double min_time(double threshold, double rate_increment, double objective, double rate = 2, double time_passed = 0){
	if (objective / rate < (threshold/rate)+objective/(rate+rate_increment)){
		return objective / rate;
	}
	double min = min_time(threshold, rate_increment, objective, rate + rate_increment, time_passed + threshold / rate);
	if (objective / rate < min + threshold / rate){
		return objective / rate;
	}
	else return threshold / rate + min;
}

int main(){
	//std::istream &input = std::cin;
	//std::ostream &output = std::cout;
	std::ifstream input_file("c:\\project\\B-small-attempt0.in");
	std::ofstream output_file("c:\\project\\B-small-attempt0.out");
	std::istream &input = input_file;
	std::ostream &output = output_file;

	int number_of_test_cases;
	input >> number_of_test_cases;
	for (int t = 1; t <= number_of_test_cases; t++){
		double threshold, rate_increment, objective;
		input >> threshold >> rate_increment >> objective;
		double min_time_taken = min_time(threshold, rate_increment, objective);
		output << "Case #" << t << ": " << std::fixed<<std::setprecision(7) << min_time_taken << std::endl;
	}
	input_file.close();
	output_file.close();
}