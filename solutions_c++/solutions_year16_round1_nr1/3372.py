#include <fstream>
#include <iostream>
#include <string>

int main(void) {
	std::ifstream fi("A-large.in");			//file in
	std::ofstream fo("A-large.out");		//file out
	if (fi.is_open())
	if (fo.is_open()) {
		std::string input;					//current line
		std::getline(fi, input);
		auto C = std::stoi(input);			//number of cases
		for (auto CC = 1; CC <= C; CC++) {	//for each(CC) case(C)
			std::getline(fi, input);		//getting case input
			std::string output = "";		//reseting variables
			output += input[0];
			for (auto i = 1; i < input.length(); i++) {
				if (input[i] >= output[0])
					output.insert(0, 1, input[i]);
				else
					output += input[i];
			}
			fo << "Case #" << CC << ": " << output << "\n";
		}
	}
	else { std::cout << "cannot open output file"; }
	else { std::cout << "cannot open input file"; }
	fi.close();
	fo.close();
	return 0;
}