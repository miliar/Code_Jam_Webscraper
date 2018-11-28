// ShyAudience.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "conio.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* inStream;
	FILE* outStream;
	errno_t err;
	err = freopen_s(&inStream, "A-large.in", "r", stdin);
	if (err != 0)
	{
		cout << "Cant open input" << endl;

		return -1;
	}
	err = freopen_s(&outStream, "My-large-practice2.out", "w", stdout);
	if (err != 0)
	{
		cout << "Cant open output" << endl;

		fclose(inStream);

		return -1;
	}
	
	int N = 0;
	cin >> N;
	for (int test_case = 1; test_case <= N; test_case++)
	{
		int sMax = 0;
		cin >> sMax;
		string s;
		vector<int> SArr;
		int ClapCount=0;
		int FrCount=0;
		SArr.resize(sMax + 1);
		
		cin>>s;
		
		for (int i = 0; i <= sMax; i++)
		{
			SArr[i] = s[i] - 48;
			if (ClapCount < i)
			{
				FrCount += i- ClapCount ;
				ClapCount += i - ClapCount ;
			}
			
			ClapCount += SArr[i];

		}
		cout <<"Case #"<<test_case<<": "<<FrCount<<endl;
	}
	/*int x;
	cin >> x;
	return 0;*/
}

