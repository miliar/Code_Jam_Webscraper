// CodeJamQ2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

#include <fstream>
#include <string> 


int mulVec(std::string str) {
	std::vector<int> vec;
	int product = 1;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '+') {
			vec.push_back(1);
		}
		else {
			vec.push_back(0);
		}
	}
	for (int i = 0; i < vec.size(); i++) {
		product = product*vec[i];
	}
	return product;
}
std::string flip(std::string str) {
	std::string s;
	int j = 0;
	int index = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] != str[i + 1]) {
			index = i;
			break;
		}
		else {
			index = str.size();
		}
	}
	if (str[index] == '+') {
		for (j = 0; j <= index; j++) {
			str[j] = '-';
		}
	}
	else {
		for (j = 0; j <= index; j++) {
			str[j] = '+';
		}
	}


	/*for (int i = j + 1; i < str.size();i++) {
		s[i] = str[i];
	}*/
	return str;
}
int turns(std::string str) {
	int multiply = mulVec(str);
	int count = 0;
	std::string s = str;
	while (multiply != 1) {
		s = flip(s);
		multiply = mulVec(s);
		count++;
	}
	return count;
}
int main()
{

	int i = 1;
	std::ifstream myfile("B-large.in");
	std::string str;
	std::ofstream outfile("new.txt");
	getline(myfile, str);
	for (std::string line; getline(myfile, line); )
	{
		int count = turns(line);
		outfile << "Case" << " #" << i << ": " << count << "\n";
		i++;
	}
    return 0;
}

