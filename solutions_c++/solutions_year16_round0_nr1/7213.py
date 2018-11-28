/*
 * count-sheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: prine
 */

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	// load case number
	fin >> CASE_NUM;
	cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 1; ti <= CASE_NUM; ti++)
	{
		int N = 0;
		fin >> N;
		cout << N << endl;

		int count = 0;
		int mark[10] = {0, };

		int i = 1;

		if (N == 0) {
			fout << "Case #" << ti << ": INSOMNIA" << endl;
		}
		else
		{
			int result = 0;
			while (count < 10) {
				result = N * i;

				int temp = result;
				while (temp != 0) {
					int last = temp % 10;
					if (mark[last] == 0) {
						mark[last]++;
						count++;
					}
					temp /= 10;
				}

				i++;
			}

			fout << "Case #" << ti << ": " << result << endl;
		}
	}

	fin.close();
	fout.close();
}

