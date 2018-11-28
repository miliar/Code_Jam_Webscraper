#include<iostream>
#include<map>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	string strFinalOutput;
	stringstream ss;
	
	int intTestCases=0, intCounter=0, j=0;
	//unsigned long long intA=0, intB=0, intSqrRootA=0, intSqrRootB=0 ;
	unsigned long long intR=0, intT=0, intCoEff=0, intExp=0, intCirclesPossible=1,intSquare=0;
	//string strNumber,strSquareNumber;
	
	outputFile.open(argv[2]);
	
	file.open(argv[1]);
	
	if(!file.eof())
	{
		file >> intTestCases;
		//cout << "\nTest = " << intTestCases;
		//unsigned long long j=0;
		
		for(int i=0; i<intTestCases; ++i){
			file >> intR;
			file >> intT;
			//intCounter=0;
			
			//cout << "\nintR = " << intR;
			//cout << "\nintT = " << intT;
			intCoEff = (2 * intR) - 1;
			intExp = (2*intR) + 1;
			intCirclesPossible=1;
			//cout << "\nintCoEff = " << intCoEff;
			//cout << "\nintExp = " << intExp;			
			while (intExp <= intT) {
				
				//cout << "\nintT = " << intT;
				intCirclesPossible++;
				intSquare = intCirclesPossible * intCirclesPossible;
				//cout << "\nintSquare = " << intSquare;
				intExp = (2 * intSquare) + (intCirclesPossible*intCoEff);
				//intCirclesPossible++;
				//cout << "\nYo - intExp = " << intExp;
			}
			
			if (j!=0) {
				ss << "\nCase #" << i+1 << ": " << intCirclesPossible-1;
				//strFinalOutput.append(ss.str());
			}
			else {
				ss << "Case #" << i+1 << ": " << intCirclesPossible-1;
				//strFinalOutput.append(ss.str());
			}
			j++;
			//strNumber="";
			//cout << "\nstrFinalOutput = " << strFinalOutput;
		}
		
	}
	
	outputFile << ss.str();
	outputFile.close();
	file.close();
	
	return 0;
	
}
