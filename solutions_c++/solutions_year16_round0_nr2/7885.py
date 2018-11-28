/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: dan
 *
 * Created on April 8, 2016, 8:10 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include <iostream>
#include <string> 

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
	if (argc < 2) return 1;

	string testcountstr = argv[1];
	uint testcount = stoi(testcountstr);

	for (uint x = 1; x < testcount + 1 && x < argc - 1; ++x) {
		string pancakestack = argv[x + 1];

		if (pancakestack.length() == 0) {
			cout << "Empty line, EOF!\n";
			return 1;
		}

		uint itercount = 0;

		while (true) {
			string::iterator testforfin = pancakestack.begin();
			while (*testforfin == '+') testforfin++;
			if (testforfin == pancakestack.end()) break;

			std::string tmpnewstring = "";

			string::iterator iterating = pancakestack.begin();
			char start = *iterating;
			while (iterating++ < pancakestack.end()) {
				if (*iterating != start) {
					string::iterator testforfin3 = iterating;
					while (testforfin3-- > pancakestack.begin()) {
						tmpnewstring += (*(testforfin3) == '+' ? '-' : '+');
					}
					break;
				}
			}

			while (iterating < pancakestack.end()) {
				tmpnewstring += *iterating++;
			}
			
			pancakestack = tmpnewstring;
			itercount++;
		}

		cout << "Case #" << x << ": " << itercount << "\n";
	}

	return 0;
}

