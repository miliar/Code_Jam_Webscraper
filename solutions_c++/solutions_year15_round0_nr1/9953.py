#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream fin("A-small-attempt1.in");
	ofstream fout("result.txt");

	string caseNumStr;
	fin >> caseNumStr;
	int caseNum = atoi(caseNumStr.c_str());

	string **caseArray = new string*[2];

	for (int i = 0; i < caseNum; i++) {
		caseArray[i] = new string[2];
		fin >> caseArray[i][0];
		fin >> caseArray[i][1];
	}

	//solve problem
	for (int i = 0; i < caseNum; i++) {
		int peopleNum = 0, peopleNeedNum = 0, peopleNeedThisTime, currentPeopleNum, currentCaseNum, currentCaseDetail;
		int currentShyness;
		string currentCaseDetaiStr = caseArray[i][1];
		currentCaseNum = atoi(caseArray[i][0].c_str());

		for (int j = 0 ; j <= currentCaseNum; j++) {
			currentPeopleNum = currentCaseDetaiStr[j] - 48;
			currentShyness = j;
			if((currentShyness != 0) && (currentShyness > peopleNum)) {
				peopleNeedThisTime = currentShyness - peopleNum;
				peopleNum += peopleNeedThisTime;
				peopleNeedNum += peopleNeedThisTime;
			}
			peopleNum += currentPeopleNum;
		}
		fout << "Case #" << i + 1 << ": " << peopleNeedNum << '\n' ;

	}


	return 0;
}