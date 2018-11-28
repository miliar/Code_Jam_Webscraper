#include<iostream>
#include<fstream>
#include<vector>
#include<map>

using namespace std;

int getCommonNumbers(int firstArray[], int secondArray[]){
	
	int commonElementCount=0, commonElement=0;
	map<int, int> myMap;
	vector<int> myVector;
	
	for (int i=0; i<4; ++i) {
		myMap[firstArray[i]]=1;		
	}
	
	for (int i=0; i<4; ++i) {
		if(myMap.find(secondArray[i]) != myMap.end()){
			commonElementCount++;
			myVector.push_back(secondArray[i]);
		}
	}
	
	if (commonElementCount==1) {
		commonElement=myVector[0];
	}else if (commonElementCount==0) {
		commonElement=0;
	}else {
		commonElement=-1;
	}

	myMap.clear();
	myVector.clear();
	
	return commonElement;
}

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;

	int myFirstArray[4][4];
	int mySecondArray[4][4];
	int firstAnswer=0, secondAnswer=0, intTestCases=0, returnValue=0;
	string finalAnswer;
	
	outputFile.open(argv[2]);
	file.open(argv[1]);

	if(!file.eof())
	{
		file >> intTestCases;
	}

	for(int t=0; t<intTestCases; ++t)
	{
		//Deal with first answer
		file >> firstAnswer;
		
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				file >> myFirstArray[i][j];
			}			
		}
		
		file >> secondAnswer;
		
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				file >> mySecondArray[i][j];
			}			
		}		
		
		returnValue = getCommonNumbers(myFirstArray[firstAnswer-1],mySecondArray[secondAnswer-1]);
		
		if (returnValue == -1) {
			if (t==0) {
				outputFile << "Case #" << t+1 << ": Bad magician!";
			}else {
				outputFile << "\nCase #" << t+1 << ": Bad magician!";
			}
		}else if (returnValue == 0) {
			if (t==0) {
				outputFile << "Case #" << t+1 << ": Volunteer cheated!";
			}else {
				outputFile << "\nCase #" << t+1 << ": Volunteer cheated!";
			}
		}else {
			if (t==0) {
				outputFile << "Case #" << t+1 << ": " << returnValue;
			}else {
				outputFile << "\nCase #" << t+1 << ": " << returnValue;
			}
		}

		
		//outputFile << "Case #" << k+1 << ": ";

	}
}