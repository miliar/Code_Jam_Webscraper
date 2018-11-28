// Copyright 2012 Alexander Krjukov. All rights reserved.

/**
 * \file Description of file, its uses and dependencies.
 * \author Alexander Krjukov (thatthissideup@gmail.com)
 */

#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>

std::set<int> extractRow(std::ifstream& infile, int rowNumber) {
	std::set<int> r;
	
	std::string line;
	
	for (int i = 0; i < rowNumber; i++) {
		//std::cout << "Ignoring row: " << i << std::endl;
		std::getline(infile, line);
	}
	
	std::clog << "Parsing row: " << rowNumber << std::endl;
	std::getline(infile, line);
	
	std::stringstream lineStream(line);
	int n;
	while (lineStream >> n) {
		r.insert(n);
	}
	
	for  (auto const& j : r) {
		std::clog << j << " ";
	}
	std::clog << std::endl;
	
	for (int i = rowNumber + 1; i <= 4; i++) {
		//std::cout << "Ignoring row: " << i << std::endl;
		std::getline(infile, line);
	}
	
	return r;
}

std::string processTestCase(std::ifstream& infile) {
	std::clog << "Processing case" << std::endl;
	
	int answer0;
	infile >> answer0;
	
	std::clog << "Answer 0: " << answer0 << std::endl;
	
	auto row0 = extractRow(infile, answer0);
	
	
	int answer1;
	infile >> answer1;
	
	std::clog << "Answer 1: " << answer1 << std::endl;
	
	auto row1 = extractRow(infile, answer1);	
	
	std::clog << std::endl;
	
	std::vector<int> intersection(4);
	
	auto it = std::set_intersection(row0.begin(), row0.end(), row1.begin(), row1.end(), intersection.begin());
	
	intersection.resize(it - intersection.begin());
	
	switch (intersection.size()) {
		case 0:
			return "Volunteer cheated!";
		case 1: {
			std::ostringstream ss;
			ss << intersection[0];
			
			return ss.str();
		}
		default:
			return "Bad magician!";
	}
}

int main() {
	std::ifstream infile("input.txt");
		
	int numCases;
	
	infile >> numCases;
	
	std::clog << "Number of cases: " << numCases << std::endl;
	
	for (int i = 0; i < numCases; i++) {
		std::cout << "Case #" << (i + 1) << ": " << processTestCase(infile) << std::endl;
	}
	
	return 0;
}