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

	for (uint x = 1; x < testcount+1 && x < argc - 1; ++x) {
		string name = argv[x+1];

		if (name.length() == 0) return 1;

		uint name_uint = stoi(name);

		uint numberstosee = 1023; // Bit fields to hold each "sheep", 10 different digits = 1111111111
		uint numbersseen = 0; // No sheep seen = 0000000000

		uint sheepcount = 0;

		bool insomnia = false;

		while ((numbersseen & numberstosee) != numberstosee) {
			uint sheepseenatstart = numbersseen;

			for (string::iterator it = name.begin(); it < name.end(); it++) {
				char numeral = *it;
				uint numberinname = numeral - '0';
				numbersseen |= (1 << numberinname);
			}

			++sheepcount;

			if (name == to_string(name_uint * (sheepcount + 1))) {
				insomnia = true;
				break;
			} else {
				name = to_string(name_uint * (sheepcount + 1));
			}
		}


		if (insomnia) {
			cout << "Case #" << x << ": INSOMNIA\n";
		} else {
			uint newname = stoi(name) - name_uint;
			cout << "Case #" << x << ": " << newname << "\n";
		}
	}

	return 0;
}

