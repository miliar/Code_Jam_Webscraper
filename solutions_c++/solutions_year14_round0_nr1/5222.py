#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
	int numTestCases;
	cin >> numTestCases;
	int row1;
	int row2;
	int rowOneValues[4];
	int rowTwoValues[4];
	string wasteSpace;
	cout << endl;
	int testResults[100];
	for(int currentTest = 1; currentTest <= numTestCases; currentTest++){
		cin >> row1;
			for(int i = 1; i < row1; i++){
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
			}
			for(int i = 0; i < 4; i++){
				cin >> rowOneValues[i];
			}
				
			for(int i = 0; i < (4 - row1); i++){
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
			}
		cin >> row2;
			for(int i = 1; i < row2; i++){
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
			}
			for(int i = 0; i < 4; i++){
				cin >> rowTwoValues[i];
			}
			
			for(int i = 0; i < (4 - row2); i++){
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
				cin >> skipws >> wasteSpace;
			}
		int magiciansNum;
		int reference;
		int matchCount = 0;
		for(int i = 0; i < 4; i++){
			reference = rowOneValues[i];
			for(int j = 0; j < 4; j++){
				if(reference == rowTwoValues[j]){
					magiciansNum = reference;
					matchCount++;
				}
			}
		}

		if(matchCount == 0){
			testResults[currentTest-1] = 0; 
		} else if(matchCount == 1){
			testResults[currentTest-1] = magiciansNum;
		} else if (matchCount > 1) {
			testResults[currentTest-1] = -1; 
		}
	}
	cout << endl;
	for(int i = 0; i < numTestCases; i++){
		cout << "Case #" << i+1 << ": ";
		if(testResults[i] == 0){
				cout << "Volunteer cheated!" << endl;
		} else if(testResults[i] == - 1){
			cout << "Bad magician!" << endl;
		} else if (testResults[i] > 0) {
			cout << testResults[i] << endl;
		}
	}
	return 0;
}
