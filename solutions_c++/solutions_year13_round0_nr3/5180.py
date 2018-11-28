// CSmall.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>

#include "Helper.h"

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream read_file;
	ofstream write_file;

	write_file.open("C:\\Users\\Matthew\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Answers\\C-small-answers.txt");
	read_file.open("C:\\Users\\Matthew\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Data Sets\\C-small-attempt1.in");
	
	CJ::Utils utils;

	int output;
	if (read_file.is_open()) 
	{
		int test_count;
		read_file >> test_count;

		unordered_set<long long> palendromes;

		for(long long kk = 0; kk < 1000; ++kk)
		{
			
			string s = std::to_string(kk);
			const char *chars = s.c_str();
			int s_len = s.length();
				
			bool is_palendrome = true;

			for(int jj = 0; jj < s_len / 2; ++jj)
				if(chars[jj] != chars[s_len - jj - 1])
					is_palendrome = false;

			if(is_palendrome)
				palendromes.emplace(kk);
		}

		for(int ii = 0; ii < test_count; ++ii)
		{
			long long low, high;
			read_file >> low;
			read_file >> high;

			auto pal_end = palendromes.end();
			int fair_sq_count= 0;

			for(long long kk = 0; kk < high; kk++)
			{
				if(palendromes.find(kk) != pal_end)
				{
					long long square = kk * kk;

					if(square >= low && square <= high && (palendromes.find(square) != pal_end))
						++fair_sq_count;
				}
			}

			write_file << "Case #" << ii + 1 << ": " << fair_sq_count << endl;
		}
	}

	read_file.close();
	write_file.close();

	return 0;
}


