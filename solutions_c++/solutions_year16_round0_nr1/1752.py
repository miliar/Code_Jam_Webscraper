// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool tab[10];
void init() {
	for (int i = 0; i < 10; ++i) {
		tab[i] = false;
	}
}
bool isOk() {
	bool res = true;
	for (int i = 0; i < 10; ++i) {
		res = res && tab[i];
	}
	return res;
}
void set(long long a) {
	while (a) {
		tab[a % 10] = true;
		a /= 10;
	}
}

int main()
{
	std::ifstream fin("in.txt");
	std::ofstream fout("out.txt");

	long long T;
	string str;

	fin >> T;

	for (int t = 1; t <= T; ++t) {

		long long  N;

		fin >> N;
		init();

		if (N == 0) {
			fout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else {
			long long n = 0;
			do {
				n += N;
				set(n);
			} while (!isOk());

			fout << "Case #" << t << ": " << n << endl;
		}


	}


    return 0;
}

