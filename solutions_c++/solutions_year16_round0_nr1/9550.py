// ConsoleApplication22.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include <vector>
using namespace std;
#include <string> 
#include <iostream>
#include <fstream>

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.out");

	//-- check if the files were opened successfully 
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;


	ios_base::sync_with_stdio(false);
	int cases = 0;
	fin >> cases;
	int times = 0;
	while (cases > 0)
	{
		times++;
		vector<bool> v;
		v.resize(10);


		int n, index;
		bool isInsomnia = true;
		fin >> n;
		
		for (int i = 1; i < 10001; ++i) {
			int temp = n * i;
			int divide = 10;
			while (temp > 0) {
				int checkNum = temp % divide;
				v[checkNum] = true;
				temp = temp / divide;
			}
			for (index = 0; index < 10; ++index) {
				if (v[index] == false)
					break;
			}
			if (index == 10) {
				isInsomnia = false;
				fout << "Case #"<< times <<": "<< n*i << endl;
				break;
			}
		}
		if (isInsomnia) {
			fout << "Case #" << times << ": " << "INSOMNIA" << endl;
		}

		cases--;
	}

    return 0;
}

