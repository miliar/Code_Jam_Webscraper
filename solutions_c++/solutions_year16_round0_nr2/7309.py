/*
 * revenge-of-the-pancakes.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: prine
 */

#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

const int MASK = 0x06; // 0110

int main(int argc, char** argv)
{
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");

	// load case number
	fin >> CASE_NUM;
	//cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 1; ti <= CASE_NUM; ti++) {
		char stack[101] = {0, };
		fin >> stack;
		int len = strlen(stack);

		//cout << stack << "(" << len << ")" << endl;

		int count = 0;

		for (int i = len; i >= 0; i--) {
			if (stack[i] == '-') {
				if (stack[0] == '+') {
					// flip all '+' from top
					char* p = stack;
					while ( *p == '+') {
						*p ^= MASK;
						p++;
					}

					count++;
				}

				// flip from top to i
				for (int j = 0; j <= i; j++)
					stack[j] ^= MASK;

				count++;
			}
		}

		fout << "Case #" << ti << ": " << count << endl;
	}

	fin.close();
	fout.close();
}
