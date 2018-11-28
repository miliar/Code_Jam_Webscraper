//
//  main.cpp
//  Google_Jam_Qualification_A
//
//  Created by Shangqi Wu on 16/4/8.
//  Copyright © 2016 Shangqi Wu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include <unordered_set>

using namespace std;

void addDigits(int n, unordered_set<int>& table) {
	
	while (n > 0) {
		
		int digit = n % 10;
		n /= 10;
		
		if (table.count(digit) == 0) {
			table.insert(digit);
		}
		
	}
	
}

int bleatrixTrotter(int n) {
	
	if (n == 0) {
		return 0;
	}
	
	long num = (int)n;
	unordered_set<int> table;
	
	while (num <= numeric_limits<int>::max()) {
		
		addDigits((int)num, table);
		
		if (table.size() == 10) {
			return (int)num;
		}
		
		num += n;
		
	}
	
	return 0;
	
}

int main(int argc, const char * argv[]) {
	
	ifstream input("./A-large.in");
	ofstream output("./output.txt");
	
	if (!input.is_open() || !output.is_open()) {
		return 1;
	}
	
	int totalNum = 0;
	int n = 0;
	input >> totalNum;
	
	for (int i = 0; i < totalNum; i++) {
		
		input >> n;
		int result = bleatrixTrotter(n);
		
		output << "Case #" << (i + 1) << ": ";
		if (result == 0) {
			output << "INSOMNIA" << endl;
		} else {
			output << result << endl;
		}
		
	}
	
	input.close();
	output.close();
	
    return 0;
}
