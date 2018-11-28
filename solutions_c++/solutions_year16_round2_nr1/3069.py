/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: dan
 *
 * Created on April 15, 2016, 20:56 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <string> 
#include <math.h>
#include <algorithm>
#include <iterator>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
	if (argc < 2) return 1;

	std::string testcountstr = argv[1];
	uint testcount = stoi(testcountstr);

	for (uint x = 2; x < testcount + 2 && x < argc; ++x) {
		std::string rearranged = argv[x];
		
		vector<std::string> validseq = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		vector<uint> validseq_int = {0,1,2,3,4,5,6,7,8,9};
		vector<uint> validnums = {};

		std::string tmprearranged = rearranged;

		//cout << "Comparing against " << tmprearranged;

		while(tmprearranged.length() > 0) {
			uint index = 0;
			bool onefound = false;
			for(std::string numtext: validseq) {
				bool allfound = true;
				std::string tmptmprearranged = tmprearranged;

				//cout << "Checking ";
				for(uint y = 0; y < numtext.length(); ++y) {
					size_t location = tmptmprearranged.find(numtext[y]);
					//cout << numtext[y];
					if(location == std::string::npos) {
						allfound = false;
						break;
					} else {
						tmptmprearranged.replace(location, 1, "");
					}
				}

				//cout << "\n";

				if(allfound) {
					//cout << "Found " << numtext << "\n";
					validnums.push_back(validseq_int[index]);
					tmprearranged = tmptmprearranged;
					onefound = true;
					break;
				}

				++index;
			}

			if(!onefound && tmprearranged.length() > 0) {
				//cout << "No matches found!\n";
				tmprearranged = rearranged;
				validnums = {};

				validseq.push_back(*validseq.begin());
				validseq.erase(validseq.begin());
				validseq_int.push_back(*validseq_int.begin());
				validseq_int.erase(validseq_int.begin());
			}

		}

		cout << "Case #" << (x - 1) << ": ";
		// ...
		
		std::sort (validnums.begin(), validnums.end());
		
		for (std::vector <uint> ::const_iterator i = validnums.begin(); i != validnums.end(); ++i)
			std::cout << *i;

		cout << "\n";
	}

	return 0;
}

