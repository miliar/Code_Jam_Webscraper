//============================================================================
// Name        : Counting_Sheep.cpp
// Author      : Mohammed Essam
// Version     : Cygwin
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int T = 0;
	int d = 0, i = 0;
	int stop = 1;
	ifstream in("A-large.in");
	ofstream out("A-large.txt");

	// Input number of Tries
	//cin >> T;
	in >> T;
	int *N = new int[T];
	int *N_res = new int[T];
	int digits[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	// Input N
	for (int z = 0; z < T; z++) {
		in >> N[z];
		N_res[z] = N[z];
	}
	for (i = 0; i < T; i++) {
		for (int j = 1; stop; j++) {
			N_res[i] = j * N[i];
			if (N[i] == 0) {
				out << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
				stop = 0;
			}
			while (N_res[i] != 0) {
				d = N_res[i] % 10;
				N_res[i] = N_res[i] / 10;
				digits[d] = 1;
			}
			for (int k = 0; k < 10; k++) {
				if (digits[k] != 1) {
					break;
				} else if (digits[k] == 1 && k == 9) {
					out << "Case #" << i + 1 << ": " << j * N[i] << endl;
					stop = 0;
				}
			}
		}
		stop = 1;
		for (int k = 0; k < 10; k++) {
			digits[k] = 0;
		}
	}
	return 0;
}
