//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <boost/algorithm/string.hpp>

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <deque>
#include <set>

#include <stdlib.h>

#include "Number.h"


// A renomer
class ProblemA {
public:

	std::set<char> vowels;

	ProblemA(){
		vowels.insert('a');
		vowels.insert('e');
		vowels.insert('i');
		vowels.insert('o');
		vowels.insert('u');
	}

	int analyse(std::string sName, int n){
		int nvalue = 0;
		std::string str = sName;
		//std::set<std::pair<int,int> > alreadyCheck;
		for(unsigned int begin = 0; begin < (sName.size()-n+1); begin++){
			for(unsigned int strsize = n; strsize < (sName.size()-begin+1); strsize++){
				//alreadyCheck.insert(std::pair<int,int>(begin, end))
				//if((end-begin)>=n){
					std::string teststr = str.substr(begin, strsize);
					if(checksubstr(teststr, n)){
						nvalue++;
					}
			//	}
			}
		}
		return nvalue;
	}

	int checksubstr(std::string str, int n){
		int t = 0;
		for(unsigned int i =0 ; i < str.size(); i++){
			if(vowels.find(str[i]) == vowels.end()){
				t++;
				if(t >= n){
					return true;
				}
			}else{
				t=0;
			}
		}
		return false;

	}

};

int main(int argc, char* argv[]) {

	if (argc == 3) {

		//fichier d'entre
		std::fstream inputFile;
		inputFile.open(argv[1]);

		//lecture nombre de test case
		std::string sNb;
		std::getline(inputFile, sNb);
		int nb = Number::getInt(sNb);

		//fichier de sortie
		std::fstream outputFile;
		outputFile.open(argv[2], std::fstream::out);

		std::fstream debugFile;
		debugFile.open("debug.log", std::fstream::out);


		ProblemA p;

		//pour chaque test case ou si l'on a atteint la fin du fichier
		for (int i = 0; (i < nb) && (inputFile.eof() == false); i++) {
			debugFile << "#"<< (i+1) << std::endl;

			//lecture parametre d'entree
			std::string testcase;
			std::getline(inputFile, testcase);
			debugFile << testcase << std::endl;
			std::vector<std::string> vTC;
			boost::split(vTC, testcase, boost::is_any_of(" "));

			outputFile << "Case #" << (i + 1) << ": "
					<< p.analyse(vTC[0], atoi(vTC[1].c_str())) << std::endl;



		}
		outputFile.close();
		debugFile.close();
		std::cout << "ok" << std::endl;
	} else {
		std::cout << "invalid number of parameter " << std::endl;
	}
	return 0;
}
