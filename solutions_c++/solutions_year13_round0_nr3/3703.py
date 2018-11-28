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

#include <stdlib.h>

#include "Number.h"

#include "ProblemC.h"

typedef std::deque<std::pair<int, bool> > deque_res;

/*int main(){
	ProblemC pc;

	std::cout << pc.palyndrome(121) << std::endl;
	std::cout << pc.palyndrome(8597) << std::endl;
	std::cout << pc.palyndrome(1257521) << std::endl;
	return 0;
}*/

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

		ProblemC pc;

		//pour chaque test case ou si l'on a atteint la fin du fichier
		for (int i = 0; (i < nb) && (inputFile.eof() == false); i++) {

			std::cout << "tc " << i << std::endl;
			//std::vector<std::string> svLine;
			std::vector<std::vector<int> > tc;

			std::string sLine;
			std::getline(inputFile, sLine);
			std::vector<int> AB = Number::getInts(sLine);

			outputFile << "Case #" << (i + 1) << ": "
					<< pc.analyse(AB[0], AB[1]) << std::endl;

		}
		outputFile.close();
		std::cout << "ok" << std::endl;
	} else {
		std::cout << "invalid number of parameter " << std::endl;
	}
	return 0;
}
