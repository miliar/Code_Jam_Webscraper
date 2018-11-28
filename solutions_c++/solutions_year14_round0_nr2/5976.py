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
		double C, F, X;
		getline(inFile, read);
		istringstream s(read);
		s >> C >> F >> X;
		double pre = X / 2;
		double now = C / 2 + X / (F + 2);
		int count = 0;
		while (now < pre){
			pre = now;
			now = now - X / (2 + F + F * count) + C / (2 + F + F * count) + X / (2 + F + F + F * count);
			count += 1;
		}

		if (now > pre)
			outFile << setprecision(15) << "Case #" << caseIter + 1 << ": " << pre << endl;
		else
			outFile << setprecision(15) << "Case #" << caseIter + 1 << ": " << now << endl;
	}
	getchar();
	return 0;
}