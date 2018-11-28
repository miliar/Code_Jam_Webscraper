// Infinite House of Pancakes.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include<stdio.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<bitset>
#include<map>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<sstream>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define REPC(I, C) for (int I = 0; (C); ++I)
#define CASET int ___t, case_n = 1; cin>>___t; while (___t-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
using namespace std;
#define SIZE 1000


int _tmain(){
	freopen("D:\\CodeJam\\a.in", "r", stdin);
	freopen("D:\\CodeJam\\a.out", "w", stdout);

	CASET{

		cout << "Case #" << case_n++ << ": ";

		int n;
		cin >> n;
		int Data[1050] = {};
		REP(i, n)
		{
			cin >> Data[i];
		}

		int nLow = 1;
		int nHigh = 2000;

		int nTimes = 0;
		while (nTimes++ < 100)
		{
			int nCur = (nLow + nHigh) / 2;

			bool bOK = false;
			for (int i = 0; i < nCur; i++)
			{
				int nSep = i;
				int nRest = nCur - i;

				int nCost = 0;
				for (int j = 0; j < n; j++)
				{
					if (Data[j]>nRest)
					{
						nCost += (Data[j] + nRest - 1) / nRest-1;
					}
				}
				if (nCost <= i)
				{
					bOK = true;
					break;
				}
			}
			
			if (bOK)
			{
				nHigh = nCur;
			}
			else
			{
				nLow = nCur;
			}
		}

		cout << nHigh << endl;
	}
	return 0;
}