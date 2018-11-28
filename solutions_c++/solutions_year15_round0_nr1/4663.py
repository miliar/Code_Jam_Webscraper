#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>

int _tmain(int argc, _TCHAR* argv[])
{
	std::wstring inputBuffer;
	std::wifstream infile;
	infile.open("A-large.in");
	std::wstring line;
	
	int numberOfTestCase = 0;
	infile >> numberOfTestCase;
	std::getline(infile, line);

	for (int i = 0; i < numberOfTestCase; i++)
	{
		std::getline(infile, line);
		std::wistringstream iss(line);
		int numAudience = 0;
		std::wstring strSi;
		if (!(iss >> numAudience >> strSi))
			break;

		int numInvites = 0;
		int numStandupAudience = 0;
		for (int i = 0; i < strSi.length(); i++)
		{
			wchar_t wc = strSi[i];
			numStandupAudience += _wtoi(&wc);
		
			if (numStandupAudience < i + 1)
			{
				int friendsToCall = i + 1 - numStandupAudience;
				numInvites += friendsToCall;
				numStandupAudience += friendsToCall;
			}
		}

		int testCase = i+1;
		std::wcout << L"Case #" << testCase << L": " << numInvites << std::endl;
	}
	infile.close();
	system("pause");
	return 0;
}