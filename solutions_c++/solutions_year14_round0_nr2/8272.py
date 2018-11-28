// Copyright 2012 Alexander Krjukov. All rights reserved.

/**
 * \file Description of file, its uses and dependencies.
 * \author Alexander Krjukov (thatthissideup@gmail.com)
 */

#include <iostream>
#include <fstream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

std::string processTestCase(std::ifstream& infile) {
	std::clog << "Processing case" << std::endl;
	
	double c, f, x;
	infile >> c >> f >> x;
	
	std::clog << "C: " << c << " F: " << f << " X: " << x << std::endl;
	
	double r = std::numeric_limits<double>::max();
	double d = 0.0f;
	
	for (int i = 0; i < 100000; i++) {
		if (i >= (100000 - 1)) {
			std::clog << "Large i" << std::endl;
		}
		double delta = 1.0f / (2.0f + (i * f));
		
		double t = x * delta + c * d;
		
		//std::clog << i << ": " << t << std::endl;
		
		d += delta;
				
		if (t > r) {
			std::clog << "Iteration count: " << i << std::endl;
			break;
		}
		r = t;
	}
	
	std::ostringstream ss;
	ss.setf(std::ios::fixed, std::ios::floatfield);
	ss.precision(7);
	ss << r;
	
	return ss.str();
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