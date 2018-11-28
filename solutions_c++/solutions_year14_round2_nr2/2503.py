#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
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

			int oldNo, newNo, catNo;
			int noWays = 0;
			getline(inputFile,line);
			vector<string> strs;
			boost::split(strs,line,boost::is_any_of(" "));

			oldNo = boost::lexical_cast<int>(strs[0]);
			newNo = boost::lexical_cast<int>(strs[1]);
			catNo = boost::lexical_cast<double>(strs[2]);


			for(int i=0; i<oldNo; i++) {
				for(int j=0; j<newNo; j++) {
					if( (i & j) < catNo) {
						noWays++;
					}
				}
			}

			outputFile << "Case #" << i+1 << ": " << noWays << endl;
		}
	}
	inputFile.close();
	outputFile.close();
}
