#include <iostream>
#include <conio.h>
#include <math.h>
#include <fstream>
#include <sstream>

using namespace std;

string toString (int number)
{
     ostringstream ss;
     ss << number;
     return ss.str();
 }
  
int main() {
	ifstream readFile;
	readFile.open("A-small-attempt0.in");
	ofstream writeFile;
	writeFile.open("p1_output.txt");

	int cases;
	int answer1, answer2;
	int arrangement[4][4];
	int resultSet1[4];
	int resultSet2[4];
	
	readFile >> cases;
	for (int i=1; i <= cases; i++) {
		int totalMatch = 0, matchNumber = 0;
		readFile >> answer1;
		
		for (int j=0; j < 4; j++) {
			for (int k=0; k < 4; k++) {
				readFile >> arrangement[j][k];
			}
		}
	
		for (int j=0; j < 4; j++) {
			resultSet1[j] = arrangement[answer1-1][j];
		}
			
		readFile >> answer2;
		
		for (int j=0; j < 4; j++) {
			for (int k=0; k < 4; k++) {
				readFile >> arrangement[j][k];
			}
		}
		
		for (int j=0; j < 4; j++) {
			resultSet2[j] = arrangement[answer2-1][j];
		}		
		
		for (int j=0; j < 4; j++) {
			for (int k=0; k < 4; k++) {
				if (resultSet1[j] == resultSet2[k]) {
					totalMatch++;
					matchNumber = resultSet1[j];
				}
			}
		}
		
		string result = "";
		if (totalMatch == 0) {
			result = "Volunteer cheated!";
		} else if (totalMatch == 1) {
			result = toString(matchNumber);
		} else {
			result = "Bad magician!";
		}
		
		writeFile << "Case #" << i << ": " << result << endl;	
	}
	
	return 0;
}
