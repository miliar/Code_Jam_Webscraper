
#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	int cases, n, sum, digits;
	bool used[10];
	
	fin >> cases;
	for (int i = 1; i <= cases; i++) {
		
		digits = 0;
		for (int t = 0; t < 10; t++)
			used[t] = false;
		
		fin >> n;
		fout << "Case #" << i << ": ";
		if (n == 0) {
			fout << "INSOMNIA" << endl;
		} else {
			sum = 0;
			do {
				sum += n;
				int t, cur_num = sum;

				while (cur_num > 0) {
					t = cur_num % 10;
					if (!used[t]) {
						used[t] = true;
						digits++;
					}
					cur_num /= 10;
				}
			} while (digits < 10);
			fout << sum << endl;
		}
	}

	fin.close();
	fout.close();
	return 0;
}
