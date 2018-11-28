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
		int nTemp;
		cin >> nTemp;
		set<int> nSet;
		int nSum = 0;
		for (int j = 0; j < 1000&& nSet.size()<10; j++)
		{
			if (nTemp==0)
				break;
			nSum += nTemp;
			int nTempSum = nSum;
			while(nTempSum>0)
			{
				nSet.insert(nTempSum%10);
				nTempSum/=10;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (nSet.size()<10)
		{
			cout << "INSOMNIA\n";
		}
		else
		{
			cout << nSum << "\n";
		}
	}
}

void q2()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string strI;
		cin >> strI;
		string strR = string(strI.size(), '+');
		int nSize = 0;
		while (strI != strR)
		{
			char cOther = strI[0]=='+'?'-':'+';
			int nPos = strI.find(cOther);
			if (nPos == -1)
			{
				nPos = strI.size();
			}
			for (int j = 0; j < nPos; j++)
			{
				strI[j] = cOther; 
			}
			nSize += 1;
		}
		cout << "Case #" << i+1 << ": ";
		cout << nSize << "\n";
	}
}

vector<int> makeprime()
{
	UINT nMax = pow(2.0,16);
	vector<int> primeTable(nMax,0);
	UINT nMaxH = pow(2.0,8);
	for (UINT i = 2; i <= nMaxH; i++)
	{
		if (primeTable[i] != 0)
		{
			continue;
		}
		UINT iNext = i;
		while (true)
		{
			iNext += i;
			if (iNext >= nMax)
			{
				break;
			}
			if (primeTable[iNext]==0)
			{
				primeTable[iNext]=i;
			}
		}
	}
	vector<int> primeArr;
	primeArr.reserve(10000);
	for (UINT i = 2; i < primeTable.size(); i++)
	{
		if (primeTable[i] == 0)
		{
			primeArr.push_back(i);
		}
	}
	return primeArr;
}

vector<UINT> createRandData(int N)
{
	vector<int> nRandArr;
	nRandArr.push_back(1);
	for (int j = 0; j < N-2; j++)
	{
		nRandArr.push_back(rand()%2);
	}
	nRandArr.push_back(1);
	vector<UINT> nDataArr(9,0);
	vector<UINT> nAdd(9,1);
	for (int j = 0; j < nRandArr.size(); j++)
	{
		for (UINT i = 2; i <= 10; i++)
		{
			if (nRandArr[j])
			{
				nDataArr[i-2] += nAdd[i-2];
			}
			nAdd[i-2]*= i;
		}		
	}
	return nDataArr;
}

int isPrime(UINT nInput, const vector<int>& primeArr)
{
	for (int i = 0; i < primeArr.size(); i++)
	{
		if (nInput%primeArr[i]==0)
		{
			return primeArr[i];
		}
	}
	return 0;
}

void q3()
{ 	
	srand((unsigned)time(0));
 	vector<int> primeArr = makeprime();
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N;
		int J;
		cin >> N >> J;
		map<UINT, vector<int>> mapR;
		while (mapR.size()<J)
		{
			vector<UINT> nDataArrT = createRandData(N);
			if (mapR.find(nDataArrT.back()) != mapR.end())
			{
				continue;
			}
			vector<int> nRArr;
			for (int j = 0; j < nDataArrT.size(); j++)
			{
				int nR = isPrime(nDataArrT[j], primeArr);
				if (nR==0)
				{
					break;
				}
				nRArr.push_back(nR);
			}
			if (nRArr.size()==9)
			{
				mapR[nDataArrT.back()] = nRArr;
			}
		}
		cout << "Case #" << i+1 << ":\n";
		for (auto a = mapR.begin(); a != mapR.end(); ++a)
		{
			cout << a->first;
			for (int j = 0; j < a->second.size(); j++)
			{
				cout << " " << a->second[j];
			}
			cout << "\n";
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//q1();
	q2();
	//q3();
	fclose(stdin);
	fclose(stdout);
	return 0;
}

