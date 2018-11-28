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

string calT1(int n, int& sum, vector<int>& nArr)
{
	if (n==2)
	{
		vector<int> nArrR;
		for (int i = 0; i < nArr.size(); i++)
		{
			if (nArr[i]>0)
			{
				nArrR.push_back(i);
			}
		}
		string strR = "";
		for (int i = 0; i < nArrR.size(); i++)
		{
			string strT = "A";
			strT[0]+=nArrR[i];
			strR += strT;
			sum -=1;
			nArr[nArrR[i]] -= 1;
		}
		return strR;
	}
	if (sum > 4)
	{
		auto a = std::max_element(nArr.begin(), nArr.end());
		int nMax = a-nArr.begin();
		sum -= 1;
		nArr[nMax]-=1;
		string strR = "A";
		strR[0]+=nMax;
		return strR;
	}
	if (sum > 2)
	{
		vector<int> nArrR;
		for (int i = 0; i < nArr.size(); i++)
		{
			if (nArr[i]>1)
			{
				nArrR.push_back(i);
			}
		}
		for (int i = 0; i < nArr.size(); i++)
		{
			if (nArr[i]>0)
			{
				nArrR.push_back(i);
			}
		}
		string strR = "";
		for (int i = 0; i < nArrR.size(); i++)
		{
			if (i<nArrR.size()-2)
			{
				sum -=1;
				nArr[nArrR[i]] -= 1;
				string strT = "A";
				strT[0]+=nArrR[i];
				strR += strT;
			}
		}
		return strR;
	}
	else
	{
		vector<int> nArrR;
		for (int i = 0; i < nArr.size(); i++)
		{
			if (nArr[i]>0)
			{
				nArrR.push_back(i);
			}
		}
		string strR = "";
		for (int i = 0; i < nArrR.size(); i++)
		{
			string strT = "A";
			strT[0]+=nArrR[i];
			strR += strT;
			sum -=1;
			nArr[nArrR[i]] -= 1;
		}
		if (sum != 0)
		{
			return "Error";
		}
		return strR;
	}
	return "Error";
}

void q1()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		cin >> n;
		vector<int> nArr(n,0);
		int sum = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> nArr[j];
			sum += nArr[j];
		}
		cout << "Case #" << i+1 << ":";
		while (sum > 0)
		{
			cout << " " << calT1(n, sum, nArr);
		}
		cout << "\n";
		//cout << strQ << "\n";
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

