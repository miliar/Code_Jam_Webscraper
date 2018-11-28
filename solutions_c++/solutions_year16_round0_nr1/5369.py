// sheepcount.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include <string>
#include <fstream>

using namespace std;
int check1s(char *, int);
int _tmain(int argc, _TCHAR* argv[])
{
	int testcase = 0;
	long long *N;
	char occ[10] = { 0 };
	ifstream infile("ip.txt");
	ofstream outfile("op.txt");
	infile >> testcase;
	if (testcase < 1 || testcase > 100){
		return 0;
	}

	N = (long long*)malloc(sizeof(long long)*testcase); 

	for (int i = 0; i < testcase; i++) {
		infile >> *(N + i);
	}

	for (int i = 0; i < testcase; i++) {
		int j = 0;
		if (*(N + i) <= 0ll || *(N + i) > 200ll) {
			outfile << "Case #" << i + 1 << ":" << " INSOMNIA"<< endl;
			continue;
		}
		while (1) {
			long long hold = (j + 1)*(*(N + i));
			while (hold != 0){
				occ[hold % 10] = 1;
				hold /= 10;
			}
			if (check1s(occ,10)) {
				outfile << "Case #" << i + 1 << ":" << " " << (j + 1)*(*(N + i)) << endl;
				memset(occ, 0, 10);
				break;
			}
			j++;
		}
		j = 0;
	}
	free(N);
	return 0;
}

int check1s(char * occ, int size) {
	for (int i = 0; i < size; i++){
		if (occ[i] == 0)
			return 0;
	}
	return 1;
}