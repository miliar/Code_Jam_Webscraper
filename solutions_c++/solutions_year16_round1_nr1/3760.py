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
#include <string> 
#include <math.h>
#include <algorithm>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
	if (argc < 2) return 1;

	std::string testcountstr = argv[1];
	uint testcount = stoi(testcountstr);

	for (uint x = 1; x < testcount + 1 && x < argc - 1; x += 1) {
		std::string input = argv[x + 1];
		std::string lastword = "";

		for (std::string::iterator i = input.begin(); i<input.end(); ++i) {
			if(lastword.size() == 0) {
				lastword += *i;	
			} else {
				if(*i >= lastword[0]) {
					lastword = *i + lastword;
				} else {
					lastword += *i;
				}
			}
		}

		cout << "Case #" << x << ": " << lastword << "\n";
	}

	return 0;
}

