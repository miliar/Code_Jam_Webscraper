//============================================================================
// Name        : MagicTrick.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
using namespace std;

int main() {
	ifstream inputFile("input.in");
	ofstream outputFile("output.out");

	string line;
	if(inputFile.is_open()) {
		getline(inputFile,line);

		int testCases = boost::lexical_cast<int>(line); //using functions from Boost library

		for(int i=0; i<testCases; i++) {

			getline(inputFile,line);
			int firstAnswer = boost::lexical_cast<int>(line);
			set<int> firstRow;

			for(int j=0; j<4; j++) {
				getline(inputFile,line);

				if(j==firstAnswer-1) {
					vector<string> strs;
					boost::split(strs,line,boost::is_any_of(" "));

					vector<string>::iterator it;
					for(it=strs.begin(); it!= strs.end(); ++it) {
						firstRow.insert(boost::lexical_cast<int>(*it));
					}
				}
			}

			getline(inputFile,line);
			int secondAnswer = boost::lexical_cast<int>(line);
			int noMatches = 0;
			int matchedNo = 0;

			for(int j=0; j<4; j++) {
				getline(inputFile,line);

				if(j==secondAnswer-1) {
					vector<string> strs;
					boost::split(strs,line,boost::is_any_of(" "));

					vector<string>::iterator it;
					for(it=strs.begin(); it!= strs.end(); ++it) {
						int cardNo = boost::lexical_cast<int>(*it);
						if(firstRow.count(cardNo) == 1 ) {
							noMatches ++;
							matchedNo = cardNo;
							if(noMatches > 1) {
								break;
							}
						}
					}
				}
			}

			if(noMatches == 0) {
				outputFile << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
			} else if (noMatches == 1) {
				outputFile << "Case #" << i+1 << ": " << matchedNo << endl;
			} else {
				outputFile << "Case #" << i+1 << ": " << "Bad magician!" << endl;
			}

		}
	}

	inputFile.close();
	outputFile.close();
	return 0;
}
