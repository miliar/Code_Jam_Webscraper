#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

//	qualification round
//	problem b - revenge of the pancakes
int main()
{
	std::wifstream infile;
	std::wofstream outFile;
	std::wistringstream iss;
	std::wostringstream oss;
	std::wstring line;

	std::wstring folderPath = L"data\\";
	std::wstring fileName = L"C-small-attempt2";
	infile.open(folderPath + fileName + L".in");
	outFile.open(folderPath + fileName + L".out.txt");

	int TotalCase = 0;
	std::getline(infile, line);
	iss.str(line);
	iss >> TotalCase;

	for (int lCnt = 0; lCnt < TotalCase; lCnt++)
	{
		//	read input
		std::getline(infile, line);
		iss.clear();
		iss.str(line);
		unsigned long N, J;
		iss >> N >> J;

		unsigned __int64 n = 1; n = n << (N - 1); n += 1;
		unsigned __int64 max = 1;	max = max << N;
		unsigned __int64 * sol = new unsigned __int64[J];
		unsigned __int64 ** divisor = new unsigned __int64 *[J];
		for (int i = 0; i < J; i++)	{
			divisor[i] = new unsigned __int64[11];
			memset(divisor[i], 0, sizeof(unsigned __int64) * 11);
		}

		int sol_cnt = 0;
		memset(sol, 0, sizeof(unsigned __int64)*J);
		
		for (; n <= max; n += 6)
		{
			bool not_prime = 1;
			for (int d = 1; d < 10; d++)
			{
				__int64 mult = 1;
				__int64 num = 0;
				for (int k = 0; k < N; k++)
				{
					unsigned __int64 tn = n >> k;
					if (tn & 1)	num += mult;
					mult *= d + 1;
				}

				unsigned __int64 div = d + 2;
				if (num % div == 0)
				{
					divisor[sol_cnt][d] = div;
				}
				else
				{
					not_prime = 0;
					break;
				}
			}
			if (not_prime)	{
				sol[sol_cnt] = n;
				sol_cnt++;
				std::wcout << sol_cnt << std::endl;
			}
			

			if (sol_cnt >= J)
				break;
		}

		//	make output
		std::wostringstream oss;
		oss << L"Case #" << lCnt + 1 << L": " << std::endl;
		for (int j = 0; j < J; j++)
		{
			//oss << sol[j] << L"\t";
			std::wstring bi;
			for (int k = 0; k < N; k++)
			{
				unsigned __int64 tt = sol[j] >> k;
				if (tt & 1)
					bi = L'1' + bi;
				else
					bi = L'0' + bi;
			}

			oss << bi;
			for (int i = 2; i <= 10; i++)
			{
				oss << L" " << divisor[j][i-1];
			}
			oss << std::endl;
		}

		delete[] sol;
		for (int i = 0; i < J; i++)
			delete[]divisor[i];
		delete[] divisor;

		std::wcout << oss.str();
		outFile << oss.str();
	}

	infile.close();
	outFile.close();
	system("pause");
	return 0;
}