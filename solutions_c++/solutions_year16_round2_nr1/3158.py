#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>

//	round 1-b
//	problem 1
int main()
{
	std::ifstream infile;
	std::ofstream outfile;

	std::string folderPath = "data\\";
	std::string fileName = "A-large";
	std::string inputfilepath = folderPath + fileName + ".in";
	infile.open(inputfilepath);
	outfile.open(folderPath + fileName + ".out.txt");
	

	int TotalCase = 0;
	infile >> TotalCase;
	for (int lCnt = 0; lCnt < TotalCase; lCnt++)
	{
		std::string s;
		std::vector<int> h(26);
		std::vector<int> d(10);
		infile >> s;
	
		for (int i = 0; i < (int)s.length(); i++){
			int tdigit = s[i] - 'A';
			h[tdigit]++;
		}

		//	zero
		int os = 'Z' - 'A';
		if (h[os] > 0)	{
			d[0] += h[os];
			h['Z' - 'A'] -= d[0];
			h['E' - 'A'] -= d[0];
			h['R' - 'A'] -= d[0];
			h['O' - 'A'] -= d[0];
		}

		//	two
		os = 'W' - 'A';
		if (h[os] > 0)	{
			d[2] += h[os];
			h['T' - 'A'] -= d[2];
			h['W' - 'A'] -= d[2];
			h['O' - 'A'] -= d[2];
		}

		//	four
		os = 'U' - 'A';
		if (h[os] > 0)	{
			d[4] = h[os];
			h['F' - 'A'] -= d[4];
			h['O' - 'A'] -= d[4];
			h['U' - 'A'] -= d[4];
			h['R' - 'A'] -= d[4];
		}

		//	six
		os = 'X' - 'A';
		if (h[os] > 0)	{
			d[6] = h[os];
			h['S' - 'A'] -= d[6];
			h['I' - 'A'] -= d[6];
			h['X' - 'A'] -= d[6];
		}

		//	eight
		os = 'G' - 'A';
		if (h[os] > 0)	{
			d[8] = h[os];
			h['E' - 'A'] -= d[8];
			h['I' - 'A'] -= d[8];
			h['G' - 'A'] -= d[8];
			h['H' - 'A'] -= d[8];
			h['T' - 'A'] -= d[8];
		}

		//	five
		os = 'F' - 'A';
		if (h[os] > 0)	{
			d[5] = h[os];
			h['F' - 'A'] -= d[5];
			h['I' - 'A'] -= d[5];
			h['V' - 'A'] -= d[5];
			h['E' - 'A'] -= d[5];
		}

		//	seven
		os = 'V' - 'A';
		if (h[os] > 0)	{
			d[7] = h[os];
			h['S' - 'A'] -= d[7];
			h['E' - 'A'] -= d[7] * 2;
			h['V' - 'A'] -= d[7];
			h['N' - 'A'] -= d[7];
		}

		//	one
		os = 'O' - 'A';
		if (h[os] > 0)	{
			d[1] = h[os];
			h['O' - 'A'] -= d[1];
			h['N' - 'A'] -= d[1];
			h['E' - 'A'] -= d[1];
		}

		//	three
		os = 'T' - 'A';
		if (h[os] > 0)	{
			d[3] = h[os];
			h['T' - 'A'] -= d[3];
			h['H' - 'A'] -= d[3];
			h['R' - 'A'] -= d[3];
			h['E' - 'A'] -= d[3];
			h['E' - 'A'] -= d[3];
		}

		//	nine
		os = 'I' - 'A';
		if (h[os] > 0)	{
			d[9] = h[os];
			h['N' - 'A'] -= d[9];
			h['I' - 'A'] -= d[9];
			h['N' - 'A'] -= d[9];
			h['E' - 'A'] -= d[9];
		}

		for (int i = 0; i < 26; i++)
			assert(h[i] >= 0);
		//__int64 sol = 0;

		std::ostringstream oss;
		oss << "Case #" << lCnt + 1 << ": ";
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < d[i]; j++)
				oss << i;
		oss << std::endl;

		std::cout << oss.str();
		outfile << oss.str();
	}
	
	outfile.close();
	system("pause");

	return 0;
}