// SleepNumber.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <math.h>


int main()
{	

	int N,T;

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	infile >> T;
	for (int iy = 1; iy <= T; iy++) {
		infile >>N;
		if (N == 0) {
			outfile << "case #" << iy << ": " << "INSOMNIA" << std::endl;
		}
		else {
			int j = 1;
			int ix = 0;
			do {
				long NN = N*j;
				int n = log10(NN);
				for (int i = 0; i <= n; i++) {
					ix = ix | (1 << (NN % 10));
					NN = NN / 10;

				}
				if (ix >= 1023) {
					outfile << "case #" << iy << ": " << N*j << std::endl;
					std::cout << N*j << std::endl;
					break;
				}
				else
					j = j + 1;

				if (j > 100) {
					outfile << "case #" << iy << ": " << "INSOMNIA" << std::endl;
					break;
				}

			} while (ix != 1023);
		} 
	}

	getchar();
	return 0;
}

