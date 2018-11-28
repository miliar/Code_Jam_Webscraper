#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define toDigit(c) (c-'0')
int totalProblemNum;
vector< vector<int>>  problemArray;

void readTxtFile(string fileName){
	string line;
	ifstream myfile (fileName);
	if (myfile.is_open()){
		bool isFirstLine=true;
		while ( getline (myfile,line) ){
			if (isFirstLine){
				isFirstLine = false;
				totalProblemNum = atoi(line.c_str());				
			}else{
				int maxLineNum = toDigit(line[0]);
				vector<int> subProblemArray;
				for (int i=2; i < 3+maxLineNum; i++)					
					subProblemArray.push_back(toDigit(line[i]));				
				problemArray.push_back(subProblemArray);
			}
			cout << line << '\n';
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
}

void writeFile(){
	ofstream myfile ("example.txt");
	if (myfile.is_open()){
		myfile << "This is a line.\n";
		myfile << "This is another line.\n";
		myfile.close();
	}
	else cout << "Unable to open file";
}

int main () {
	
	//read Problem txt file
	readTxtFile("../A-small-attempt1.txt");
	cout << "\n" << "\n";

	ofstream myfile ("problem1Result.txt");
	if (myfile.is_open()){
		for(int i = 0 ; i< totalProblemNum ; i++){
			int diffMax=0;
			int Smax = problemArray[i].size()-1;			
			int tmpSum=0;
			for (int j=0; j<problemArray[i].size() ; j++){
				tmpSum += problemArray[i][j];
				if(j+1 > tmpSum){
					int diff = j+1 - tmpSum;
					if(diffMax <= diff) diffMax = diff;
				}
			}
			
			myfile << "Case #" << i+1 << ": " << diffMax<< "\n";		
		}
	}
	return 0;
}