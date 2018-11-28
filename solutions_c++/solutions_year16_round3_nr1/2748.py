#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>

int getMajorParty(int Party[], int counted[], int N)	{
	int maxParty = 0;
	int maxIdx = -1;
	for (int i = 0; i < N; i++)	{
		if (counted[i])
			continue;
		if (maxParty < Party[i])	{
			maxParty = Party[i];
			maxIdx = i;
		}
	}
	assert(maxIdx > -1);
	return maxIdx;
}

int main_ca()
{
	std::ifstream infile;
	std::ofstream outfile;

	std::string folderPath = "data\\";
	std::string fileName = "A-small-attempt0";
	std::string inputfilepath = folderPath + fileName + ".in";
	infile.open(inputfilepath);
	outfile.open(folderPath + fileName + ".out.txt");


	int TotalCase = 0;
	infile >> TotalCase;
	for (int lCnt = 0; lCnt < TotalCase; lCnt++)
	{
		int sol = 0;
		int N = 0;
		int p[26] = { 0 };
		int count[26] = { 0 };

		infile >> N;
		for (int i = 0; i < N; i++)	{
			infile >> p[i];
		}

		int p1 = getMajorParty(p, count, N);
		count[p1] = 1;
		int p2 = getMajorParty(p, count, N);
		
		std::string partout;

		//	1. 다수당 1,2 를 동수로 만든다.
		while (p[p1] > p[p2])	{
			partout += 'A' + p1;
			partout += " ";
			p[p1]--;
		}

		//	2. 나머지 당원들 대피
		for (int i = 0; i < N; i++)	{
			if (i == p1 || i == p2)
				continue;

			if (p[i] > 0)	{
				for (int j = 0; j < p[i]/2; j++)	{
					partout += 'A' + i;
					partout += 'A' + i;
					partout += " ";
				}
				if (p[i] % 2)	{
					partout += 'A' + i;
					partout += " ";
				}
			}
		} 


		//	3. 다수당 1,2 동시 대피
		for (int i = 0; i < p[p1]; i++)	{
			partout += 'A' + p1;
			partout += 'A' + p2;
			partout += " ";
		}

		std::ostringstream oss;
		oss << "Case #" << lCnt + 1 << ": ";
		//oss << sol;
		oss << partout;
		oss << std::endl;

		std::cout << oss.str();
		outfile << oss.str();
	}

	outfile.close();
	system("pause");

	return 0;
}