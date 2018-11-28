// a.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
	int t;
	ifstream ifile;
	ofstream ofile;
	ofile.open("ans.out");
	ifile.open("A-large.in");
	ifile >> t;
	//cin >> t;

	for (int i = 1; i <= t; i++)
	{
		int a;
		ifile >> a;
		//cin >> a;
		int table[10] = { 0 };
		if (a == 0)
		{
			//printf("Case #%d: INSOMNIA\n", i);
			ofile << "Case #" << i << ": INSOMNIA" << endl;
		}
		else 
		{
			long long n = 1;
			while (true)
			{
				bool flag = true;
				long long ans = n*a;
				string ans_str = to_string(ans);
				for (int inner_i = 0; inner_i < ans_str.size(); inner_i++)
				{
					table[ans_str[inner_i] - '0']++;
				}
				for (int inner_i = 0; inner_i < 10; inner_i++)
				{
					if (table[inner_i] == 0)
					{
						flag = false;
						break;
					}
				}
				if (flag)
				{
					//printf("Case #%d: %d\n", i, ans);
					ofile << "Case #" << i << ": " << ans << endl;
					break;
				}
				n++;
			}
		}
	}
	
	


    return 0;
}

