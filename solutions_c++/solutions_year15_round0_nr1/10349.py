//============================================================================
// Name        : gogle.cpp
// Author      : Manav
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include<math.h>
std::ifstream infile("thefile.in");
using namespace std;
int ovation() {
	int S, i, *ptr, n = 0, t = 0;
	unsigned long int num;

	infile >> S;

	ptr = (int*) malloc(sizeof(int) * S);

	infile >> num;
	for (i = S; i >= 0; i--) {
		ptr[i] = num % 10;
		num = num / 10;
	}
	for (i = 0; i <= S; i++) {
		if (ptr[i] != 0) {

			if (i > 0) {
				if (i > t) {
					n = n + i - t;
					t = t + i - t;

				}

			}
			t = t + ptr[i];
		}
	}

	free(ptr);
	return n;
}
int main() {
	ofstream outfile;
	outfile.open("output.out");

	int t, i, *ptr;
	if (infile.fail()) {
		cerr << "Error Opening File" << endl;
		exit(1);
	}
	infile >> t;

	ptr = (int*) malloc(sizeof(int) * t);

	for (i = 0; i < t; i++)
		ptr[i] = ovation();

	for (i = 0; i < t; i++)
		outfile<< "Case #"<<i+1<<": "<<ptr[i]<<endl;
	outfile.close();

		free(ptr);

	return 0;
}
