#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file;
    ofstream outputFile;
	
    int intTestCases = 0;
	int intN = 0;
	long long currentValue = 0;
	long long previousValue = 0;
	long long minMushCase1 = 0;
	long long minMushCase2 = 0;
	long long maxDifference = 0;
	long long currentDifference = 0;
	
	vector<long long> myVector;

    outputFile.open(argv[2]);
    file.open(argv[1]);
	
    if (!file.eof()) {
        file >> intTestCases;
    }
	
	myVector.clear();
	
    for (int t=0; t<intTestCases; ++t) {
		minMushCase1 = 0;
		minMushCase2 = 0;
		previousValue = 0;
		currentValue = 0;
		maxDifference = 0;
		currentDifference = 0;
		
		file >> intN;
		
		for (int i=0; i<intN; ++i) {
			previousValue = currentValue;
			file >> currentValue;
			myVector.push_back(currentValue);
			
			if (previousValue > currentValue) {
				currentDifference = previousValue - currentValue;
				minMushCase1 = minMushCase1 + currentDifference;
				if (currentDifference > maxDifference) {
					maxDifference = currentDifference;
				}
			}
		}
		
		for (int i=0; i<intN-1; ++i) {
			if (myVector.at(i) < maxDifference) {
				minMushCase2 = minMushCase2 + myVector.at(i);
			} else {
				minMushCase2 = minMushCase2 + maxDifference;
			}

		}
				
		if (t==0) {
            outputFile << "Case #" << t+1 << ": " << minMushCase1 << " " << minMushCase2;
        } else {
            outputFile << "\nCase #" << t+1 << ": " << minMushCase1 << " " << minMushCase2;
        }
		myVector.clear();
	}
}
	
