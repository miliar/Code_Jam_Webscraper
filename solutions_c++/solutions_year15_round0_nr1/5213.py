#include<iostream>
#include<string>
#include<vector>
//#include<stdlib.h>
#include"readFile.cpp"

int main(int argc, char** argv){
	
	std::vector<std::string> contents;

	std::ofstream outputFile ("A_Small.txt");

	unsigned sMax = 0;
	unsigned numPeople = 0;
	unsigned numAdded = 0;

	if(argc != 2){

		std::cout << "Improper number of arguments..." << std::endl;

		return 0;
	}

	contents = getStrings(argv[1]);

	//Code goes here...

	for(unsigned i = 1; i < contents.size(); i++){

		sMax = contents[i][0] - '0';

		numPeople = contents[i][2] - '0';

		for(unsigned j = 1; j <= sMax; j++){

			if((contents[i][(2 + j)] - '0') != 0){

				if(numPeople >= j){

					numPeople += (contents[i][(2 + j)] - '0');
				}
				else{

					numAdded += j - numPeople;
					numPeople = j + (contents[i][(2 + j)] - '0');
				}
			}
		}

		outputFile << "Case #" << i << ": " << numAdded << std::endl;

		sMax = 0;
		numPeople = 0;
		numAdded = 0;
	}


	outputFile.close();

	return 0;
}
