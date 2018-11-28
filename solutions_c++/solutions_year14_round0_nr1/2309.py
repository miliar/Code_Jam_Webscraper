#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

int compareRow(int *firstNums, int firstRow, int *secondNums, int secondRow, int n)
{
    vector<int> sameNums;
    for(int i = 4 * firstRow; i != 4 * firstRow + 4 && i != n; ++i) {
        for(int j = 4 * secondRow; j != 4 * secondRow + 4 && j != n; ++j) {
            if(firstNums[i] == secondNums[j]) {
                sameNums.push_back(firstNums[i]);
            }
        }
    }

    if(sameNums.size() == 1) {
        return sameNums[0];
    }
    else if(sameNums.size() == 0) {
        return 0;
    }
    else {
        return -1;
    }
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile(outputFileName.c_str(), ios::out | ios::trunc);
	if (!inputFile || !outputFile) {
		cout << "Open file error" << endl;
		return -2;
	}
    string line;
    getline(inputFile, line);
	int caseNum = atoi(line.c_str());
	int i = 0; 
	while (i < caseNum) {
        int firstRow, secondRow;
        int firstNums[16];
        int secondNums[16];
        getline(inputFile, line);
        firstRow = atoi(line.c_str()) - 1;
        for(int j = 0; j != 4; ++j) {
            getline(inputFile, line);
            stringstream ss;
            ss.str(line);
            ss >> skipws >> firstNums[4 * j] >> firstNums[4 * j + 1]  >> firstNums[4 * j + 2] >> firstNums[4 * j + 3];
        }
            
        getline(inputFile, line);
        secondRow = atoi(line.c_str()) - 1;
        for(int j = 0; j != 4; ++j) {
            getline(inputFile, line);
            stringstream ss;
            ss.str(line);
            ss >> secondNums[4 * j] >> secondNums[4 * j + 1]  >> secondNums[4 * j + 2] >> secondNums[4 * j + 3];
        }

        int num = compareRow(firstNums, firstRow, secondNums, secondRow, 16);
        stringstream ss;
        if(num == 0) {
            ss << "Volunteer cheated!";
        }
        else if(num == -1) {
            ss << "Bad magician!";
        }
        else {
            ss << num;
        }
        outputFile << "Case #" << ++i << ": " << ss.str() << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
