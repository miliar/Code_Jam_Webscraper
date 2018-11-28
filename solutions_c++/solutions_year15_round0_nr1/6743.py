#include <algorithm>
#include <string>
#include <vector>
#include <stdlib.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cassert>
#include <sstream>
#include <iomanip>

int main (int argc, char* argv[]){
	
	if (argc < 3) return 1;
	
	std::ifstream in_str(argv[1]);
	std::ofstream out_str(argv[2]);
	
	std::string line = "";
	std::stringstream ss;
	std::string str = "";
	
	getline(in_str, line);
	unsigned int numcases = std::atoi(line.c_str());
	unsigned int testcase = 1;
	
	unsigned int S = 0, N = 0, k = 0, add = 0;
	int friends = 0;
	std::string crowd = "";
	
	while (numcases > 0){
		
		getline(in_str, line);
		ss.clear();
		ss << line;
		
		assert(ss >> S);
		assert(ss >> crowd);
		ss.clear();
		k = 0;
		friends = 0;
		N = 0;
		
		for (unsigned int i = 0; i < crowd.size(); i++){
			if (crowd[i] == '1') add++;
			else if (crowd[i] == '2') add += 2;
			else if (crowd[i] == '3') add += 3;
			else if (crowd[i] == '4') add += 4;
			else if (crowd[i] == '5') add += 5;
			else if (crowd[i] == '6') add += 6;
			else if (crowd[i] == '7') add += 7;
			else if (crowd[i] == '8') add += 8;
			else if (crowd[i] == '9') add += 9;
			
			if (k > 0 && add > 0 && k > N) {friends += (k - N); N += (k - N);}
			N += add;
			add = 0;
			k++;
		}
		
		out_str << "Case #" << testcase << ": " << friends;
		if (numcases > 1) out_str << "\n";
		
		testcase++;
		numcases--;
		crowd.clear();
	}
}