// A.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <memory.h>
using namespace std;

int solve(string s)
{
	int i;
	int result = 0;
	if (s[s.length() - 1] != 48)
	{
		for (i = s.length() - 1; i >= 0; i--)
		{
			result *= 10;
			result += s[i]-48;
		}
		return result;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string s;
	int *arr = new int[1000001];
	memset(arr, 0, sizeof(int) * 1000001);
	
	int i,test;
	
	for (i = 1; i <= 1000000; i++)
	{
		s = std::to_string(i);
		test = solve(s);
		if (arr[i] != 0)
		{
			arr[i] = (arr[i - 1] + 1 > arr[i]) ? arr[i] : arr[i - 1] + 1;
		}
		else
		{
			arr[i] = arr[i-1] + 1 ;
		}

		if (test != 0)
		{
			if (test > i && test <= 1000000)
			{
				arr[test] = arr[i] + 1;
			}
		}
	}
	int T,number;

	cin >> T;
	int t = 1;
	while (T--)
	{
		cin >> number;

		printf("Case #%d: %d\n",t++,arr[number]);
	}

	return 0;
}

