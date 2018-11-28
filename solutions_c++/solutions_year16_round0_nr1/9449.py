// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

#include <fstream>
#include <string> 


std::vector<int> killDuplicates(std::vector<int> N) {
	std::vector<int> killDuplicates;
	std::sort(N.begin(), N.end());
	std::unique_copy(N.begin(), N.end(), std::back_inserter(killDuplicates));
	return killDuplicates;

}
int countVec(std::string s) {
	std::vector<int> vec;
	for (int i = 0; i < s.size(); i++) {
		vec.push_back(s[i] - '0');
	}
	std::vector<int> killDuplicate = killDuplicates(vec);
	int count = 0;
	for (int i = 0; i < killDuplicate.size(); i++) {
		count = count + killDuplicate[i];
	}
	return count;
}
int mulVec(std::string s) {
	std::vector<int> vec;
	for (int i = 0; i < s.size(); i++) {
		vec.push_back(s[i] - '0');
	}
	std::vector<int> killDuplicate = killDuplicates(vec);
	int count = 1;
	for (int i = 0; i < killDuplicate.size(); i++) {
		count = count * killDuplicate[i];
	}
	return count;
}
int countSheep(int N) {
	std::string s = std::to_string(N);
	int count = countVec(s);
	int c = 0;
	int m = 1;
	int multiplyFactor = 2;
	bool condition = true;
	if (N == 0) {
		N = 0;
	}
	else {
		while (condition) {
			if (count == 45 && m == 0) {
				condition = false;
				
			}
			else {
				c = N*multiplyFactor;
				s = s + std::to_string(c);
				count = countVec(s);
				m = mulVec(s);

				multiplyFactor++;
			}
		}
	}
	return c;
}

int main()
{
	int i = 1;
	std::ifstream myfile("A-large.in");
	std::string str;
	std::ofstream outfile("new.txt");
	getline(myfile, str);
	for (std::string line; getline(myfile, line); )
	{
		int count = countSheep(atoi(line.c_str()));
		if (count == 0) {
			outfile << "Case" << " #" << i << ": " << "INSOMNIA" << "\n";
		}
		else {
			outfile << "Case" << " #" << i << ": " << count << "\n";
		}
		i++;
	}
	/*int y = 11;
	int count = countSheep(1692);
	std::cout << "count" << count;*/
	return 0;
}

