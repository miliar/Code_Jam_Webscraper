#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

bool isPal(const int& num){

	string dumNum;
	int spot = 0;
	int mod = 10;
	int analysisNum = num;

	while((num % mod) != num){

		dumNum[spot] = ((analysisNum % mod) / (mod / 10));
		analysisNum -= (analysisNum % mod);
		mod *= 10;
		spot++;
	}

	dumNum[spot] = ((analysisNum % mod) / (mod / 10));

	for(int i = 0; i < ((spot + 2) / 2); i++){

		if(dumNum[i] != dumNum[(spot - i)]){

			return 0;
		}
	}

	return 1;
}

int main(){

	ifstream in_file;
	in_file.open("smallC.txt");

	string number;

	in_file >> number;

	char* dum = &number[0];

	int numCases = atoi(dum);

	int lowBound = 1;
	int highBound = 1000;

	for(int i = 0; i < numCases; i++){

		in_file >> number;
		dum = &number[0];
		lowBound = atoi(dum);
		in_file >> number;
		dum = &number[0];
		highBound = atoi(dum);

		int squareBase = 1;
		int square = 1;
		int squareJump = 3;

		while(square < lowBound){

			squareBase++;
			square += squareJump;
			squareJump += 2;
		}

		int count = 0;

		while(square <= highBound){

			if(isPal(squareBase) && isPal(square)){

				count++;
			}

			squareBase++;
			square += squareJump;
			squareJump += 2;
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}

