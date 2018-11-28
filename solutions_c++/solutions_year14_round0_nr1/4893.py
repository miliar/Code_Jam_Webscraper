#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

struct CardSet{
	int attOne;
	int gridOne[4][4];
	int attTwo;
	int gridTwo[4][4];
};

int checkGuess(int *, int *);

int main(){
	ifstream inputFile;
	const char *fileName = "A-small-attempt0.in";
	inputFile.open(fileName);//change filename to input file
	ofstream outputFile("gcj2014_answer1.txt");
	int caseNumber = 0; 
	int tempInt = 0; //file read-in
	string s = "";
	int guessOne[4] = {0,0,0,0};
	int guessTwo[4] = {0,0,0,0};
	int magicNumber = 0;

	if (inputFile.is_open()){
		// read the case number first
		inputFile  >> tempInt;
		caseNumber = tempInt;
		// init cardsets with the given number
		CardSet* instance = new CardSet[caseNumber];
		string* result = new string[caseNumber];
		for (int i=0; i<caseNumber; ++i){
			// for every case, load the input into struct Cardset
			inputFile >> tempInt;
			instance[i].attOne = tempInt - 1;
			for (int j=0; j<16; ++j){
				inputFile >> tempInt;
				instance[i].gridOne[j/4][j%4] = tempInt;//fetch input int into grid[][]
			}
			inputFile >> tempInt;
			instance[i].attTwo = tempInt - 1;
			for (int j=0; j<16; ++j){
				inputFile >> tempInt;
				instance[i].gridTwo[j/4][j%4] = tempInt;
			}			
		}
		//calculate the magic
		for (int i=0; i<caseNumber; ++i){
			for (int j=0; j<4; ++j){
				guessOne[j] = instance[i].gridOne[instance[i].attOne][j];
			}

			for (int j=0; j<4; ++j){
				guessTwo[j] = instance[i].gridTwo[instance[i].attTwo][j];
			}
			magicNumber = checkGuess(guessOne, guessTwo);
			//convert the magic number to string for output purpose
			stringstream ss;
			ss << magicNumber;
			string str = ss.str();
			//Generate Answer
			switch(magicNumber){
				case 0: 
					result[i] = "Bad magician!";
					break;
				case -1: 
					result[i] = "Volunteer cheated!";
					break;
				default:
					result[i] = str;
					break;
			}
			// cout<<result[i]<<endl;
		}
		//output to answer file
		if (outputFile.is_open()){
			for (int i=0; i<caseNumber; ++i)
				//Output the case into answer file under instruction
				outputFile << "Case #" << i+1 << ": " << result[i] << endl;
		}
		outputFile.close();
		delete[] instance;
		delete[] result;
	}
	inputFile.close();
	return 0;
}

int checkGuess(int *guessOne, int *guessTwo){
	int count = 0;
	int number = 0;
	for (int i=0; i<4; ++i){
		for (int j=0; j<4; ++j)
		if (guessOne[i] == guessTwo[j]){
			count ++;
			if (count > 1)
				return 0;
			number = guessOne[i];
		}
	}
	//return number if there's only one answer, other wise return status
	if (count == 1){
		return number;
	}
	else 
		return -1;
}