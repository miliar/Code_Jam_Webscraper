#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int testcases = 0;
	int arrangement1[4][4];
	int arrangement2[4][4];
	
	int rowFirstAnswer[4];
	int rowSecondAnswer[4];
	int firstAnswer = 0;
	int secondAnswer = 0;
	
	cin >> testcases;
    cin.ignore(1, '\n');

	for(int i = 0; i < testcases; i++){
		//Read arrangement
		cin >> firstAnswer;
    	cin.ignore(1, '\n');
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin >> arrangement1[j][k];
				if(j == (firstAnswer-1)){
					rowFirstAnswer[k] = arrangement1[j][k];
				}
			}
			cin.ignore(1, '\n');
		}
				//Read arrangement
		cin >> secondAnswer;
    	cin.ignore(1, '\n');
		for(int m = 0; m < 4; m++){
			for(int n = 0; n < 4; n++){
				cin >> arrangement2[m][n];
				if(m == (secondAnswer-1)){
					rowSecondAnswer[n] = arrangement2[m][n];
				}
			}
			cin.ignore(1, '\n');
		}
		
		bool found = false;
		bool found_many = false;
		int number = -1;
		
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(rowFirstAnswer[i] == rowSecondAnswer[j]){
					number = rowFirstAnswer[i];
					if(found){
						found_many=true;
						break;
					}
					else{
						found = true;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": ";  
		if(found_many){
			cout << "Bad magician!";
		}
		else if(number == -1){
			cout << "Volunteer cheated!";
		}
		else{
			cout << number;
		}
		if(i != testcases-1){
			cout << endl;
		}
	}
	
	return 0;
}