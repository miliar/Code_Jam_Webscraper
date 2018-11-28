#include <vector>
#include <cmath>
#include <map>
#include <utility>
#include <stdint.h>
#include <iostream>
#include <string>
#include<iostream>
#include<fstream>

std::map<char, int> abc;

void insert(std::string& str, char c, bool antes) {
	if (antes) {
		str.insert(str.begin(), c);
	}
	else {
		str.push_back(c);
	}
}

void func1(std::string input) {
	std::string new_str;
	new_str.push_back(input[0]);
	for (int i = 1; i < input.size(); i++) {
		if (new_str[0] > input[i]) {
			insert(new_str, input[i], false);
		}
		else {
			insert(new_str, input[i], true);
		}
	}
	printf("%s\n", new_str.c_str());
}


int main(int argc, const char * argv[]) {

	std::ifstream myfile("input.txt");
	std::string buffer;
	int i = 1;
	int m;
	myfile >> m;
	while (!myfile.eof()) {
		myfile >> buffer;
		printf("Case #%d: ", i++);
		func1(buffer);
	}

	return 0;
}