#include <iostream>

using namespace std;


int main(){
	int numberOfTestCases;
	int firstChosenLine;
	int secondChosenLine;
	cin >> numberOfTestCases;
	int firstNumbers[4];
	int secondNumbers[4];
	int matchingNumbers = 0;
	int matchingNumber;
	int caseNumber = 0;
	int trash;
	while(numberOfTestCases--){		
		caseNumber++;
		matchingNumbers = 0;
		cin >> firstChosenLine;
		int line = 0;
		while(line != 4){
			if(line == (firstChosenLine-1)){				
				cin >> firstNumbers[0] >> firstNumbers[1] >> firstNumbers[2] >> firstNumbers[3];
			}else{				
				cin >> trash >> trash >> trash >> trash;
			}
			line++;
		}
		cin >> secondChosenLine;
		line = 0;
		while(line != 4){
			if(line == (secondChosenLine-1)){
				cin >> secondNumbers[0] >> secondNumbers[1] >> secondNumbers[2] >> secondNumbers[3];
			}else{
				cin >> trash >> trash >> trash >> trash;
			}
			line++;
		}

		for(int i=0; i < 4; i++){
			for(int j=0; j<4; j++){
				if(firstNumbers[i] == secondNumbers[j]){
					matchingNumbers++;
					matchingNumber = firstNumbers[i];
				}
			}
		}
		if(matchingNumbers == 0){
			cout << "Case #" << caseNumber << ": Volunteer cheated!\n";
		}else{
				if(matchingNumbers == 1){
					cout<< "Case #" << caseNumber << ": " << matchingNumber << "\n";
				}else{
					if(matchingNumbers > 1){
						cout << "Case #" << caseNumber << ": Bad magician!\n";
					}				
			}
		}

	}
	return 0;
}