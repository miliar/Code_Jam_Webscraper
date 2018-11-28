#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;
using std::vector;

const int SIZE = 4;

void getRow(int row, int array[], ifstream &inputFile);
void printResult(int trialNum, vector<int> &answer, ofstream &outputFile);

int main()
{
	ifstream inputFile;
	ofstream outputFile;
	outputFile.open("output.txt");
	inputFile.open("input.txt");
	int firstRow[SIZE];
	int secondRow[SIZE];
	vector<int> answer;
	
	int trials;
	int count = 0;
	int row;
	string tempLine;
	stringstream line;
	getline(inputFile, tempLine);
	line << tempLine;
	line >> trials;
	//cout << trials << endl;
	while (++count <= trials) {
		line.clear();
		line.str("");
		getline(inputFile, tempLine);
		line << tempLine;
		line >> row;
		/*for (int x = 0; x < SIZE; x++) {
			getline(inputFile, tempLine);
			line << tempLine;			
			if (x == row - 1) {
				//for (int y = 0; y < SIZE; y++);
				line >> firstRow[0] >> firstRow[1] >> firstRow[2] >> firstRow[3];
				cout << "1st Row: " << line.str() << endl;	
			}
			line.clear();
			line.str("");
		}*/
		line.clear();
		line.str("");	
		getRow(row, firstRow, inputFile);	
		getline(inputFile, tempLine);
		line << tempLine;
		line >> row;
		/*for (int x = 0; x < SIZE; x++) {
			getline(inputFile, tempLine);
			line << tempLine;			
			if (x == row - 1) {
				//for (int y = 0; y < SIZE; y++);
				line >> secondRow[0] >> secondRow[1] >> secondRow[2] >> secondRow[3];
				cout << "2nd Row: " << line.str() << endl;	
			}
			line.clear();
			line.str("");
		}*/
		getRow(row, secondRow, inputFile);
	
		for (int x = 0; x < SIZE; x++) {
			for (int y = 0; y < SIZE; y++)
				if (firstRow[x] == secondRow[y])
					answer.push_back(firstRow[x]);
		}
		printResult(count, answer, outputFile);
		answer.clear();
	}

	inputFile.close();
	outputFile.close();
	return 0;
}

void getRow(int row, int array[], ifstream &inputFile)
{
	string temp;
	stringstream line;

	for (int x = 0; x < SIZE; x++) {
		getline(inputFile, temp);
		line << temp;
		if (row - 1 == x) {
			line >> array[0] >> array[1] >> array[2] >> array[3];
			cout << "Row " << row << ": " << line.str() << endl;
		}
		line.clear();
		line.str("");
	}
}

void printResult(int trialNum, vector<int> &answer, ofstream &outputFile)
{
	outputFile << "Case #" << trialNum << ": ";
	if (answer.size() == 0)
		outputFile << "Volunteer cheated!" << endl;
	else if (answer.size() == 1)
		outputFile << answer[0] << endl;
	else
		outputFile << "Bad magician!" << endl; 
}
