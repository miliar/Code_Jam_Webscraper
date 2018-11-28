#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

//	qualification round
//	problem a - counting sheep
int main()
{
	std::wifstream infile;
	std::wofstream outFile;
	std::wistringstream iss;
	std::wostringstream oss;
	std::wstring line;

	std::wstring folderPath = L"C:\\Users\\Administrator\\Desktop\\";
	std::wstring fileName = L"A-small-attempt3";
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

		__int64 N = 0;
		iss >> N;

		//	solve
		__int64 sol = 0;

		//double trivia = 0.1e-6;
		int cnt[10] = { 0 };
		int max[10] = { 0, 10, 45, 10, 45, 18, 50, 10, 45, 10 };
		int last_digit = 0;
		int mcnt = 0;
		for (mcnt = 1; mcnt < 10; mcnt++)
		{
			__int64 m = mcnt * N;
			std::wostringstream toss;
			toss << m;
			std::wstring bash = toss.str();
			for (int i = bash.length() - 1; i >= 0; i--)
			{
				last_digit = bash[i] - '0';
				if (last_digit)
					break;
			}

			if (last_digit == 1 || last_digit == 3 || last_digit == 7 || last_digit == 9)
				break;
		}

		for (int i = 0; i < max[last_digit] * mcnt; i++)
		{
			__int64 m = (i + 1)*N;
			std::wostringstream toss;
			toss << m;
			std::wstring bash = toss.str();
			for (int j = bash.length() - 1; j >= 0; j--)
			{
				int c = bash[j] - '0';
				cnt[c]++;
			}

			for (int j = 0; j < 10; j++)
			{
				if (cnt[j] == 0)
					break;
				if (j == 9)
					sol = m;
			}
			if (sol > 0)
				break;
		}

		//	make output
		std::wostringstream oss;
		oss << L"Case #" << lCnt + 1 << L": ";
		if (sol == 0)
			oss << L"INSOMNIA";
		else
			oss << sol;

		std::wcout << oss.str() << std::endl;
		outFile << oss.str() << std::endl;
	}
	
	infile.close();
	outFile.close();
	system("pause");
	return 0;
}