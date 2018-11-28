// t1.cpp : �������̨Ӧ�ó������ڵ㡣
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
	UINT nMaxH = pow(2.0,9);
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
		if (nInput<=primeArr[i])
		{
			return 0;
		}
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


bool createRandDataR(int N, string& nR, vector<int>& nDataArrT, const vector<int>& primeArr)
{
	vector<int> nRandArr;
	nRandArr.push_back(1);
	int nSum = 0;
	for (int j = 0; j < N-3; j++)
	{
		int nTemp = rand()%2;
		nRandArr.push_back(nTemp);
		nSum += nTemp;
	}
	nRandArr.push_back(nSum%2);
	nRandArr.push_back(1);
	nSum += nSum%2;
	nSum += 2;
	if (nSum%3!=0)
	{
		return false;
	}
	if ((nSum*6)%10!=4)
	{
		return false;
	}
	int n81 = 0;
	int n82 = 0;
	UINT n2 = 0;
	UINT n4 = 0;
	int nAdd81 = 1;
	int nAdd82 = 1;
	int nAdd2 = 1;
	int nAdd4 = 1;
	for (int j = 0; j < nRandArr.size(); j++)
	{
		if (nRandArr[j])
		{
			n2 += nAdd2;
			n4 += nAdd4;
			n81 += nAdd81;
			n82 += nAdd82;
		}
		nR = string(nRandArr[j]?"1":"0")+nR;
		nAdd81*= 8;
		nAdd82*= 8;
		nAdd2*=2;
		nAdd4*=4;
		nAdd81 %=10;
		nAdd82 %=3;
	}
	n81%=10;
	int n8 = 0;
	if (n81==5)
	{
		n8 = 5;
	}
	else if (n82%3==0)
	{
		n8 = 3;
	}
	else
	{
		return false;

	}
	int nP2 = isPrime(n2, primeArr);
	if (nP2==0)
	{
		return false;
	}
	int nP4 = isPrime(n4, primeArr);
	if (nP4==0)
	{
		return false;
	}
	for (int i = 2; i <=10; i++)
	{
		if (i%2==1)
		{
			nDataArrT.push_back(2);
			continue;
		}
		if (i == 6)
		{
			nDataArrT.push_back(5);
			continue;
		}
		if (i == 10)
		{
			nDataArrT.push_back(3);
			continue;
		}
		if (i == 8)
		{
			nDataArrT.push_back(n8);
			continue;
		}
		if (i==2)
		{
			nDataArrT.push_back(nP2);
			continue;
		}
		if (i==4)
		{
			nDataArrT.push_back(nP4);
			continue;
		}
	}
	return true;
}

void q3B()
{
	int T;
	cin >> T;
	vector<int> primeArr = makeprime();
	for (int i = 0; i < T; i++)
	{
		int N;
		int J;
		cin >> N >> J;
		map<string, vector<int>> mapR;
		while (mapR.size()<J)
		{
			vector<int> nDataArrT;
			string strT;
			if (!createRandDataR(N,strT, nDataArrT, primeArr))
			{
				continue;
			}
			if (mapR.find(strT) != mapR.end())
			{
				continue;
			}
			mapR[strT] = nDataArrT;
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

void q4()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int K,C,S;
		cin >> K >> C >> S;
		cout << "Case #" << i+1 << ":";
		if (S+C-1<K)
		{
			cout << " IMPOSSIBLE\n";
		}
		else
		{
			UINT nBegin = 1;
			for (int j = 1; j < min(K,C); j++)
			{
				nBegin = (nBegin-1)*K+j+1;
			}
			int nLess = K-C+1;
			if (nLess <1)
			{
				nLess = 1;
			}
			for (int j = 0; j < nLess; j++)
			{
				cout << " " << j+nBegin;
			}
			cout <<"\n";
		}
	}

}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//q1();
	//q2();
	//q3();
	//q3B();
	q4();
	fclose(stdin);
	fclose(stdout);
	return 0;
}

