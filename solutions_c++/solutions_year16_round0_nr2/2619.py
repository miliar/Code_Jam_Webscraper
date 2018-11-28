#include <iostream>
#include <fstream>
#include <string>

int count(std::string str) {
	int acc = 0;
	if (str.size() == 0) return 0;
	char last = str[0];
	for (unsigned int j = 1; j<str.size();j++) {
		if (last != str[j]) acc++;
		last = str[j];
	}
	if (last == '-') acc++;
	return acc;
}

int main(int argc, char **argv) {
	int t;
	std::ifstream input;
	std::ofstream output;
	
	input.open("B-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		std::string n;
		input >> n;
		output << "Case #" << i << ": ";
		output << count(n);
		output << std::endl;
	
	}
    input.close();
	output.close();
	return 0;
}
