#include<iostream>
#include<string>
#include<fstream>
#include<string.h>
using namespace std;

int main(){
	ifstream myfile("A-small-attempt0.in");
	ofstream outfile("output.out");
	string line;
	int testCases;
	int  caseNum = 1;
	if (myfile.is_open())
	{
		getline(myfile, line);
		testCases = stoi(line);
		while (myfile.good())
		{
			int firstChoice;
			getline(myfile, line);
			firstChoice = stoi(line);
			firstChoice--;
			int first[4][4];
			int choiceRow1[4];
			for (int i = 0; i < 4; i++){
				for (int j = 0; j < 4; j++){
					if (j < 3){
						getline(myfile, line, ' ');
						first[i][j] = stoi(line);
					}
					else{
						getline(myfile, line);
						first[i][j] = stoi(line);
					}
					if (i == firstChoice){
						choiceRow1[j] = first[i][j];
					}
				}
			}
			int secondChoice;
			getline(myfile, line);
			secondChoice = stoi(line);
			secondChoice--;
			int second[4][4];
			for (int i = 0; i < 4; i++){
				for (int j = 0; j < 4; j++){
					if (j < 3){
						getline(myfile, line, ' ');
						second[i][j] = stoi(line);
					}
					else{
						getline(myfile, line);
						second[i][j] = stoi(line);
					}
				}
			}
			int ans;
			int checkers = 1;
			for (int i = 0; i < 4; i++){
				for (int j = 0; j < 4; j++){
					if (second[secondChoice][j] == choiceRow1[i]){
						ans = choiceRow1[i];
						checkers++;
					}
				}
			}
			if (checkers == 2){
				outfile << "Case #" << caseNum << ": " << ans << endl;
			}
			else if (checkers>2){
				outfile << "Case #" << caseNum << ": Bad magician!" << endl;
			}
			else if (checkers == 1){
				outfile << "Case #" << caseNum << ": Volunteer cheated!" << endl;
			}
			caseNum++;
		}
		myfile.close();
	}

	else cout << "Unable to open file";

	return 0;
}
