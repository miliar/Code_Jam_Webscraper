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
	int t;
	fin >> t;
	int n, j;
	fin >> n >> j; 
	fout << "Case #1:"<<"\n";
	for (int m = 0; m < t; m++)
	{
		unsigned long long cur = pow(10, 15) + 1;
		while (j)
		{
			bitset<16> foo = bitset<16>(cur);
			int flag = 0;
			int res[9] = {0};
			for (int rep = 2; rep < 11; rep++)
			{
				unsigned long long num = 0;
				for (int i = 0; i < 16; i++)
				{
					num += pow(rep*foo[i], i);					
				}//cout << num <<" ";
				if (fmod(num, 2) == 0)
				{
					res[rep - 2] = 2;
					flag += 1;
				}
				else
				{
					for (int h = 3; h < sqrt(num); h += 2) {
						int p = 0;
						if (num % h == 0) {
							res[rep - 2] = h;
							flag += 1; p = 1;
						}
						if (p)
							break;
					}
				}//cout << foo << "\n";
			}
			
			if (flag >= 9)
			{
				//cout << j << "\n";
				j--;
				//cout << foo;
				fout << foo <<foo;
				for (int i = 0; i < 9; i++)
				{
					//cout << " " << res[i];
					fout << ' ' << res[i];
				}
				//cout << "\n";
				fout << "\n";
			}
			cur+=2;	
			
		}
	}
	//cin >> t;
	fout.close();
	
}