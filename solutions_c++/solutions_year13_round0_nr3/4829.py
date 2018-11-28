/*
 * forsmall_main.cpp
 *
 *  Created on: 2013-4-13
 *      Author: chenjd
 */

#include <iostream>
#include <fstream>

using namespace std;

int main()
{

	int T;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin >> T;

	int a[6] = { 1, 4, 9, 121, 484};
	int test_case;
	for (test_case = 1; test_case <= T; test_case++)
	{
		int A, B;
		int sub_a = -1, sub_b = -1;
		fin >> A >> B;
		for (int i = 0; i < 5; i++)
		{
			if (A <= a[i])
			{
				sub_a = i;
				break;
			}
		}
		if (sub_a == -1)
			sub_a = 5;
		for (int i = 0; i < 5; i++)
		{
			if (B < a[i])
			{
				sub_b = i;
				break;
			}
		}
		if (sub_b == -1)
			sub_b = 5;
	fout<<"Case #"<<test_case<<": "<<sub_b-sub_a<<endl;
	}

	return 0;
}
