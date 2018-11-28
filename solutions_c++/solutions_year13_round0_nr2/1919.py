#include<iostream>
#include<vector>
#include<fstream>
#include<string>

using namespace std;

bool funcCheckEqual (vector<vector<int> > &inputVector, vector<vector<int> > &outputVector, int intN, int intM)
{	
	for (int j=0; j<intN; ++j) {
		for (int k=0; k<intM; ++k) {
			if (inputVector[j][k] != outputVector[j][k]) {
				return false;
			}	
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	vector<vector<int> > inputVector;
	vector<vector<int> > outputVector;
	vector<int> intRowMaxVector;
	vector<int> intColMaxVector;
	
	int intTestCases=0, intN=0, intM=0, x=0, maxElement=0;
	outputFile.open(argv[2]);

	file.open(argv[1]);

	if(!file.eof())
	{
		file >> intTestCases;
	
		for(int i=0; i<intTestCases; ++i){
			file >> intN;
			file >> intM;
			
			//Set row vector and column vector
			intRowMaxVector.resize(intN);
			intColMaxVector.resize(intM);
			
			//Set memory for two dimensional array of size N * M
			inputVector.resize(intN);
			outputVector.resize(intN);
			for (int j=0; j<intN; ++j){
				inputVector[j].resize(intM);
				outputVector[j].resize(intM);
			}
			
			//Row Loop
			for (int j=0; j<intN; ++j) {
				maxElement = 0;
				for (int k=0; k<intM; ++k) {
					file >> inputVector[j][k];	
					
					if (inputVector[j][k] > maxElement) {
						maxElement = inputVector[j][k];
					}
				}
				intRowMaxVector[j] = maxElement;
			}

			//Column Loop
			for (int j=0; j<intM; ++j) {
				maxElement = 0;
				for (int k=0; k<intN; ++k) {
					if (inputVector[k][j] > maxElement) {
						maxElement = inputVector[k][j];
					}
				}
				intColMaxVector[j] = maxElement;
			}
			
			for (int j=0; j<intN; ++j) {
				for (int k=0; k<intM; ++k) {
					outputVector[j][k] = intRowMaxVector[j];
				}
			}
			
			for (int j=0; j<intM; ++j) {
				for (int k=0; k<intN; ++k) {
					if (outputVector[k][j] > intColMaxVector[j]) {
						outputVector[k][j] = intColMaxVector[j];
					}
				}
			}
				
			if(funcCheckEqual(inputVector,outputVector,intN,intM)){
				if (i!=0) {
					outputFile << "\nCase #" << i+1 << ": YES";
				}
				else {
					outputFile << "Case #" << i+1 << ": YES";
				}

			}else {
				if (i!=0) {
					outputFile << "\nCase #" << i+1 << ": NO";
				}else {
					outputFile << "Case #" << i+1 << ": NO";
				}

			}
			inputVector.clear();
			outputVector.clear();
			intRowMaxVector.clear();
			intColMaxVector.clear();
		}
	
	
	}
	
	outputFile.close();
	file.close();
	
	return 0;

}


