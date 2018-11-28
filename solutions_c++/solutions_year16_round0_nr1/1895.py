#include "stdafx.h"

#include <fstream>
#include <sstream>

#include <iostream>
#include <string>
#include <vector> 
#include <algorithm>
#include <map>
#include <stack>
#include <bitset>         // std::bitset

using namespace std;

int main()
{
	int m = 1;
	ifstream fin;
	fin.open("in.in");
	ofstream fout;
	fout.open("output.txt");

	int max = 2;
	int t;
	fin >> t;
	for (int m = 0; m < t; m++)
	{

		int n;
		fin >> n; //cout << n << "\n";
		int flags[10] = { 0 };
		//cout << n;

		//res[n] = (i - 1);
		//fout << (i - 1) << ", ";
		//cout << n << " " << ((i - 1)*n) << " " << (i-1) << "\n";
		//max = (i - 1) > max ? (i - 1) : max;*/
		if (n == 0)
		{
			fout << "Case #" << (m + 1) << ": " << "INSOMNIA" << "\n";
		}
		else
		{
			bool flag = false;
			int i = 1;
			while (!flag)
			{
				int k = i*n;
				//cout << k << "\n";
				while (k)
				{
					flags[k % 10] = 1;
					k /= 10;
				}flag = true;
				for (int i = 0; i < 10; i++)
				{


					if (!flags[i])
					{
						flag = false;
					}
				}
				i++;
			}
			fout << "Case #" << (m + 1) << ": " << n*(i - 1) << "\n";

		}

	}
	fout.close();
	
}