/*
Google Code Jam
Qualification Round
4-11-14
Name: Robert Gonzalez
Problem: A. Magic Trick

*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;


vector<string> result;

void findCard(int hand1[4][4], int hand2[4][4], int firstPick, int secondPick, int caseNum);
void print_to_file();

int main(int argc, char * argv[]){
	
	int numTestCases = 0;		//Number of test cases, each with two grids being dealt
	int numFstPick;			//Volunteers first number
	int numSecPick;			//Volunteers second number
	int firstHand[4][4];
	int secondHand[4][4];
	int caseNumber = 1;

	ifstream input;
	input.open("input.txt");

	string buff;
	if(input.is_open()){
		input >> buff;			//Get Number of test cases
		numTestCases = atoi(buff.c_str());		//Convert to integer and store
		while(numTestCases != 0){
			input >> buff;
			numFstPick = atoi(buff.c_str());		//Number first chosen by volunteer

			for(int i = 0; i < 4; i++)				//Grab first grid
				for(int j = 0; j < 4; j++){
					input >> buff;
					firstHand[i][j] = atoi(buff.c_str());
				}

				input >> buff;
				numSecPick = atoi(buff.c_str());

			for(int i = 0; i < 4; i++)				//Grab secon grid
				for(int j = 0; j < 4; j++){
					input >> buff;
					secondHand[i][j] = atoi(buff.c_str());
				}
				//Figure out the trick
				findCard(firstHand,secondHand,numFstPick,numSecPick,caseNumber);
				caseNumber++;
				numTestCases--;
		}	
	input.close();		//Close file when complete
	}
	else{
		cerr << "File could not be opened" << endl;
		return -1;
	}

	//Output results to file
	print_to_file();

	return 0;
}


//Find card and store result 
void findCard(int hand1[4][4], int hand2[4][4], int firstPick, int secondPick, int caseNum){

	firstPick--;
	secondPick--;
	int cnt = 0;
	int card = -1;
	int val;
	//cout << "First: " << firstPick << endl << "Second: " << secondPick << endl << endl;
	for(int i = 0; i < 4; i++){
		 val = hand1[firstPick][i];
			for(int j = 0; j < 4; j++){
				//cout << val << " == " << hand2[secondPick][j] << endl;
				if(val == hand2[secondPick][j]){
					cnt++;
					card = val;
				}
			}
	}

		//Volunteer Cheated
	if(cnt == 0){
		ostringstream tmpnum;
		tmpnum << "Case #" << caseNum << ": Volunteer cheated!";
		result.push_back(tmpnum.str());
		return;
	}

		//Bad Magician
	if(cnt >= 2){
		ostringstream tmpnum;
		tmpnum << "Case #" << caseNum << ": Bad magician!";
		result.push_back(tmpnum.str());
		return;
	}

		//Success Good Trick
	if( cnt == 1){
		ostringstream tmpnum;
		tmpnum << "Case #" << caseNum << ": " << card;
		result.push_back(tmpnum.str());
		return;
	}
	
	//2 or more match, bad magician
	//0 match volunteer
}


void print_to_file(){

	ofstream output;
	output.open("result.txt");

	if(output.is_open()){
		for(int i = 0; i < result.size(); i++){
			output << result[i] << endl;
			cout << result[i] << endl;
		}
	}
	else
		cout << "ERROR: could not print result" << endl;


	output.close();


}