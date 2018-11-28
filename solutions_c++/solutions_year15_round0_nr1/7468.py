// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, _TCHAR* argv[])
{
	string line;
	int testCase;
	int i=0,j=0;
	int maxShy;
	int spacePos;
	ifstream inputFile("A-large.in");
	ofstream outputFile("output.txt");
	int shyFirst;
	int stood;
	int invited;

	getline(inputFile,line);
	testCase= std::stoi(line);
	
	for(i=0;i<testCase;i++){
		getline(inputFile,line);
		spacePos=line.find_first_of(" ");
		cout<<spacePos;
		maxShy=stoi(line.substr(0,spacePos));
		cout<<maxShy;
		shyFirst=stoi(line.substr(spacePos+1,1));
		stood=shyFirst;
		invited=0;
		cout << shyFirst;
		for(j=1;j<=maxShy;j++){
			if(stood<j){
				invited+=j-stood;
				stood+=stoi(line.substr(spacePos+j+1,1))+j-stood;
			} else{
				stood+=stoi(line.substr(spacePos+j+1,1));
			}
		}
		outputFile << "Case #"<<(i+1)<<": "<<invited<<"\n"; 
	}
	inputFile.close();
	outputFile.close();
	return 0;
}

