// t1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <intsafe.h>

#define UINT ULONG64

using namespace std;

void q1()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string strT;
		cin >> strT;
		string strQ;
		strQ += strT[0];
		for (int j = 1; j < strT.size(); j++)
		{
			if (strQ[0] <= strT[j])
			{
				strQ = strT[j]+strQ;
			}
			else
			{
				strQ += strT[j];
			}
		}
		cout << "Case #" << i+1 << ": ";
		cout << strQ << "\n";
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	q1();
	fclose(stdin);
	fclose(stdout);
	return 0;
}

