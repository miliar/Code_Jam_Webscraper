#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

#define toDigit(c) (c-'0')
int totalProblemNum;
vector< vector<int>>  problemArray;

void readTxtFile(string fileName){
	string line;
	ifstream myfile (fileName);
	bool isOdd=true;
	if (myfile.is_open()){
		bool isFirstLine=true;
		int maxLineNum;
		while ( getline (myfile,line) ){
			
			if (isFirstLine){
				isFirstLine = false;
				totalProblemNum = atoi(line.c_str());				
			}else{							
				if(isOdd){				
					isOdd = false;
					maxLineNum = toDigit(line[0]);
				}else{
					isOdd=true;
					vector<int> subProblemArray;
					for (int i=0; i < maxLineNum*2; i = i+2)					
						subProblemArray.push_back(toDigit(line[i]));				
					problemArray.push_back(subProblemArray);
				}
			}
			//cout << line << '\n';
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

int findMax(vector<int> tmpArray){
	int maxNum=0;
	for (int i=0 ; i<tmpArray.size() ; i++)
		if(maxNum<tmpArray[i]) maxNum = tmpArray[i];	
	return maxNum;

}

int main () {
	
	//read Problem txt file
	readTxtFile("B-small-attempt0.txt");
	cout << "\n" << "\n";

	ofstream myfile ("problem2Result_small.txt");
	if (myfile.is_open()){
		for(int i = 0 ; i< totalProblemNum ; i++){				
			int maxPancakeNum = 0;
			maxPancakeNum = findMax(problemArray[i]);	
			int totalTime=1000001;
			for (int j=1; j<maxPancakeNum+1 ; j++){
				int numOfSplit =0;
				for (int k=0; k<problemArray[i].size(); k++){
					if(problemArray[i][k]>j) 
						numOfSplit += (problemArray[i][k]-0.01f)/j;					
				}
				int tmpTotalTime = numOfSplit+j;
				if (totalTime >tmpTotalTime){
					totalTime = tmpTotalTime;
				}
			}
			myfile << "Case #" << i+1 << ": " << totalTime<< "\n";		
			//cout << "Case #" << i+1 << ": " << totalTime<< "\n";		
		}
	}
	return 0;
}