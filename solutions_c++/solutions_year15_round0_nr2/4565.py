#include<iostream>
#include<fstream>
#include<queue>
#include<math.h>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file;
    ofstream outputFile;
	
    int intTestCases = 0;
	int intD = 0;
	int currentValue = 0;
	priority_queue<int> myPQ;
	priority_queue<int> mySecondPQ;
	
	int bestTime = 0;
	int timeElapsed = 0;
	int halfValue = 0;
	int firstPart = 0;
	int secondPart = 0;
	int specialTime = 0;
	int currentElement = 0;
	int worstCase = 0;
	double half = 0.0;

    outputFile.open(argv[2]);
    file.open(argv[1]);
	
    if (!file.eof()) {
        file >> intTestCases;
    }
	
    for (int t=0; t<intTestCases; ++t) {
		bestTime = 0;
		specialTime = 0;
		timeElapsed = 0;
		file >> intD;
		
		for (int i=0; i<intD; ++i) {
			file >> currentValue;
			myPQ.push(currentValue);
			mySecondPQ.push(currentValue);
		}
		
		bestTime = myPQ.top();
		worstCase = bestTime;
		
		while (!myPQ.empty()) {
			currentElement = myPQ.top();
			
			// Scenario just to complete as-is
			if ((timeElapsed + currentElement) < bestTime) {
				bestTime = timeElapsed + currentElement;
			}
			
			// Taking special time scenario
			specialTime++;
			timeElapsed++;
			
			half = ((double)currentElement/2);
			halfValue = ceil(half);
			
			if (halfValue > 1) {
				myPQ.push(halfValue);
				myPQ.push(currentElement - halfValue);
			}
			myPQ.pop();
		}
		
		//cout << "After first iteration: Best time " << bestTime;
		timeElapsed = 0;
		specialTime = 0;
		while (!mySecondPQ.empty()) {
			currentElement = mySecondPQ.top();
			//cout << "\nCurrent Top value is : " << currentElement;
			
			// Scenario just to complete as-is
			if ((timeElapsed + currentElement) < bestTime) {
				bestTime = timeElapsed + currentElement;
			}
			
			// Taking special time scenario
			specialTime++;
			timeElapsed++;
			
			if (currentElement >=2 ) {
				if ((currentElement % 2) == 0) {
					firstPart = currentElement/2;
					secondPart = currentElement - firstPart;
				} else {
					half = ((double)currentElement/2);
					//cout << "\nCurrent half is : " << half;
					halfValue = ceil(half);
					
					//cout << "\nCurrent halfValue is : " << halfValue;
					if ((halfValue % 2) == 0) {
						firstPart = halfValue;
						secondPart = currentElement - firstPart;
					} else {
						firstPart = halfValue + 1;
						secondPart = currentElement - firstPart;
					}
				}
				
				//cout << "\nCurrent firstPart is : " << firstPart;
				//cout << "\nCurrent secondPart is : " << secondPart;
				if (firstPart > 1) {
					mySecondPQ.push(firstPart);
					mySecondPQ.push(secondPart);
				}
			}
			mySecondPQ.pop();
			
		}
		
		
		
		
		
		
		
		/*while (!myPQ.empty()) {
			currentElement = myPQ.top();
			//cout << "\nCurrent Top value is : " << currentElement;
			
			// Scenario just to complete as-is
			if ((timeElapsed + currentElement) < bestTime) {
				bestTime = timeElapsed + currentElement;
			}
			
			// Taking special time scenario
			specialTime++;
			timeElapsed++;
			
			if (currentElement >=2 ) {
				if ((currentElement % 2) == 0) {
					firstPart = currentElement/2;
					secondPart = currentElement - firstPart;
				} else {
					half = ((double)currentElement/2);
					cout << "\nCurrent half is : " << half;
					halfValue = ceil(half);
				
					cout << "\nCurrent halfValue is : " << halfValue;
					if ((halfValue % 2) == 0) {
						firstPart = halfValue;
						secondPart = currentElement - firstPart;
					} else {
						firstPart = halfValue + 1;
						secondPart = currentElement - firstPart;
					}
				}

				cout << "\nCurrent firstPart is : " << firstPart;
				cout << "\nCurrent secondPart is : " << secondPart;
				if (firstPart > 1) {
					myPQ.push(firstPart);
					myPQ.push(secondPart);
				}
			}
			myPQ.pop();

		}*/
		
		
		

		
		if (t==0) {
            outputFile << "Case #" << t+1 << ": " << bestTime;
        } else {
            outputFile << "\nCase #" << t+1 << ": " << bestTime;
        }
		
	}
}
	
