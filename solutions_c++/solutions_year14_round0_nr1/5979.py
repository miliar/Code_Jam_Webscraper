#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <map>
#include <stdlib.h>
#include <iomanip> 

using namespace std;

int findNum(int i, int a1, int a2, int a3, int a4){
	if (i == a1 || i == a2 || i == a3 || i == a4)
		return 1;
	else
		return 0;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	string read;
	int tempInt;
	inFile.open("input.txt");
	outFile.open("output.txt");
	getline(inFile, read);
	int caseNumber = atoi(read.c_str());
	for (int caseIter = 0; caseIter != caseNumber; ++caseIter){
		vector<int> temp1, temp2;
		int i1, i2, i3, i4;
		getline(inFile, read);
		int line1 = atoi(read.c_str());
		for (int i = 0; i != 4; ++i){
			getline(inFile, read);
			if (line1 == i + 1){
				istringstream s(read);
				s >> i1 >> i2 >> i3 >> i4;
			}
		}
		int i5, i6, i7, i8;
		getline(inFile, read);
		int line2 = atoi(read.c_str());
		for (int i = 0; i != 4; ++i){
			getline(inFile, read);
			if (line2 == i + 1){
				istringstream s(read);
				s >> i5 >> i6 >> i7 >> i8;
			}
		}
		if (findNum(i1, i5, i6, i7, i8) + findNum(i2, i5, i6, i7, i8) + findNum(i3, i5, i6, i7, i8) + findNum(i4, i5, i6, i7, i8) > 1)
			outFile << "Case #" << caseIter + 1 << ": Bad magician!" << endl;
		else{
			if (findNum(i1, i5, i6, i7, i8) == 1)
				outFile << "Case #" << caseIter + 1 << ": " << i1 << endl;
			else if (findNum(i2, i5, i6, i7, i8) == 1)
				outFile << "Case #" << caseIter + 1 << ": " << i2 << endl;
			else if (findNum(i3, i5, i6, i7, i8) == 1)
				outFile << "Case #" << caseIter + 1 << ": " << i3 << endl;
			else if (findNum(i4, i5, i6, i7, i8) == 1)
				outFile << "Case #" << caseIter + 1 << ": " << i4 << endl;
			else
				outFile << "Case #" << caseIter + 1 << ": Volunteer cheated!" << endl;
		}
	}
	getchar();
	return 0;
}