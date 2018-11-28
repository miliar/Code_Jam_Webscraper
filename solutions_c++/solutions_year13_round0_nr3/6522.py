// Q3.cpp : 定義主控台應用程式的進入點。
//

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int pArray[] = {1,4,9,121,484,10201};	// palindrome and squre under 1000

int solve(ifstream &ifile) {
	int min, max;
	ifile >> min >> max;
	int pSize = sizeof(pArray) / sizeof(int);

	int min_index = 0;
	int max_index = pSize-1;

	for(int i=0;i<pSize;++i) {
		if(min <= pArray[i]) {
			min = pArray[i];
			min_index = i;
			break;
		}
	}

	for(int i=0;i<pSize;++i) {
		if(max < pArray[i]) {
			if(i > 0) {
				max = pArray[i-1];
				max_index = i-1;
			}
			break;
		}
	}

	return max_index - min_index + 1;
}

int main(int argc, char* argv[])
{
	ifstream ifile("c_in.txt");
	ofstream ofile("c_out.txt");

	int case_num;
	ifile >> case_num;
	for(int i=0;i<case_num;++i) {
		int res = solve(ifile);
		char buffer[1024];
		sprintf(buffer, "Case #%d: %d", i+1, res);
		ofile << buffer << endl;
	}

	system("PAUSE");
	return 0;
}
