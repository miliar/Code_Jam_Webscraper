#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class ProblemA {
public:
    string solve(int firstSelection, const vector<vector<int> > &firstGrid, int secondSelection, const vector<vector<int> > &secondGrid) {
	vector<int> firstRowSelection = firstGrid[firstSelection];
	vector<int> secondRowSelection = secondGrid[secondSelection];
	
	sort(firstRowSelection.begin(), firstRowSelection.end());
	sort(secondRowSelection.begin(), secondRowSelection.end());
	bool found;
	int numberOfOccurance = 0;
	vector<int> occuranceVector;
	for(int i = 0; i < firstRowSelection.size(); i++) {
	    found = binary_search(secondRowSelection.begin(), secondRowSelection.end(), firstRowSelection[i]);
	    if (found) {
		numberOfOccurance++;
		occuranceVector.push_back(firstRowSelection[i]);
	    }
	}
	if (numberOfOccurance == 1) {
	    stringstream ss;
	    ss << occuranceVector[0];
	    return ss.str();
	} else if (numberOfOccurance == 0) {
	    return "Volunteer cheated!";
	} else {
	    return "Bad magician!";
	}
    }
};

const int MAX_NUMBER_ROWS = 4;

int main(int argc, char **argv) {
    ifstream inputFile ("A-small-attempt1.in");
    ofstream outputFile ("output.txt");
    
    string buffer;
    int numberOfTestCases, firstSelection, secondSelection;
    
    if (inputFile.is_open()) {
	getline(inputFile, buffer);
	stringstream(buffer) >> numberOfTestCases;
	
	for(int testCaseN = 0; testCaseN < numberOfTestCases; testCaseN++) {
	    getline(inputFile, buffer);
	    stringstream(buffer) >> firstSelection;
	    vector<vector<int> > firstGrid;
	    vector<vector<int> > secondGrid;
	    ProblemA a;
	    for( int i = 0; i < MAX_NUMBER_ROWS; i++) {
		getline(inputFile, buffer);
		stringstream vectorStream(buffer);
		int x;
		firstGrid.push_back(vector<int>());
		while( vectorStream >> x) {
		    firstGrid.back().push_back(x);
		}
	    }
	    getline(inputFile, buffer);
	    stringstream(buffer) >> secondSelection;
	    for( int i = 0; i < MAX_NUMBER_ROWS; i++) {
		getline(inputFile, buffer);
		stringstream vectorStream(buffer);
		int x;
		secondGrid.push_back(vector<int>());		
		while( vectorStream >> x) {
		    secondGrid.back().push_back(x);
		}
	    }
	    outputFile << "Case #" << testCaseN + 1 << ": " <<  a.solve(firstSelection - 1, firstGrid, secondSelection - 1, secondGrid);
	    outputFile << endl;
	}
    }
    outputFile.close();
    inputFile.close();
    return 0;
}
