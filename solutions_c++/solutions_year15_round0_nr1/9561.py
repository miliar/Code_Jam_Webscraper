#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

vector<int> convertToArray(string input){
	vector<int> output;
	const char * inputArray = input.c_str();

	for (int i = 0; i < input.length(); i++)
	{
		output.push_back(inputArray[i] - '0');
	}

	for (int i = 0; i < output.size(); i++)
	{
		cout << output[i];
	}
	cout << endl;

	return output;
	
}

vector<vector<int>> processInputFile(char * fileName){
	vector<vector<int>> inputData;

	ifstream inputFile(fileName);
	string inputLine;
	bool firstLine = true;
	int numberOfTestCases = 0;

	while (getline(inputFile, inputLine)){

		if (firstLine){
			stringstream temp(firstLine);
			temp >> numberOfTestCases;
			firstLine = false;
		}
		else{
			string maxShyness, inputString;
			stringstream temp(inputLine);
			temp >> maxShyness >> inputString;
			vector<int> output;
			
			const char * inputArray = inputString.c_str();

			for (int i = 0; i < inputString.length(); i++)
			{
				output.push_back(inputArray[i] - '0');
			}

			inputData.push_back(output);
		}
	}

	return inputData;


}


void processData(vector<vector<int>> & inputData, vector<int>&  outputData){

	
	
	for (int i = 0; i < inputData.size(); i++)
	{
		int length = inputData[i].size();
		vector<int> opt(length);
		int initialTotal = 0;
		for (int j = 0; j < length; j++)
		{
			initialTotal += inputData[i][j];
			if (j == 0){
				opt[j] = inputData[i][j];
			}
			else{
				if (j <= opt[j - 1]){
					opt[j] = inputData[i][j] + opt[j - 1];
				}
				else{
					opt[j] = inputData[i][j] + j;
				}
			}
		}
		outputData.push_back(opt[length - 1] - initialTotal);
	}
	/*
	for (int i = 0; i < inputData.size(); i++)
	{
		int length = inputData[i].size();
		for (int j = 0; j < length; j++)
		{
			cout << inputData[i][j] << " ";
		}
		cout << "output" << outputData[i]<<endl;

	}
	*/

}

void writeToFile(const vector<int>& outputData){
	ofstream outputFile("output");

	for (int i = 0; i < outputData.size(); i++){
		//Case #1: 0
		stringstream outputStringtemp1;
		stringstream outputStringtemp2;
		string outputString;

		outputString = "Case #";
		
		outputStringtemp1 << i+1;
		outputString += outputStringtemp1.str();
		
		outputString += ": ";
		
		outputStringtemp2 << outputData[i];
		outputString += outputStringtemp2.str();

		outputFile << outputString  << endl;
	}
}

int main(int argc, char* argv[]){
	
	vector<vector<int>> inputData;
	vector<int> outputData;
	inputData = processInputFile(argv[1]);
	processData(inputData, outputData);
	writeToFile(outputData);
	
	return 0;
}