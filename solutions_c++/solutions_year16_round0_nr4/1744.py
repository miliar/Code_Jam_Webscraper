// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <ctgmath>

using namespace std;

int main()
{
	std::ifstream fin("in.txt");
	std::ofstream fout("out.txt");

	long long T;
	string str;

	fin >> T;

	for (int t = 1; t <= T; ++t) {

		long long  K, C, S;

		fin >> K >> C >> S;

		long long pa = pow(K, C - 1);

		fout << "Case #" << t << ":";

		for (int k = 0; k < K; ++k) {
			fout << " " << (pa * k + 1);
		}

		fout << endl;

	}


    return 0;
}

