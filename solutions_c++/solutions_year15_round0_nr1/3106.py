// Standing Ovation.cpp : 定义控制台应用程序的入口点。
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
		string strData;
		cin >> n;
		cin >> strData;

		int ans = 0;
		int nCount = strData[0]-'0';

		for (int i = 1; i <= n; i++)
		{
			if (nCount < i)
			{
				ans += i - nCount;
				nCount = i;
			}

			nCount += strData[i] - '0';
		}
		cout <<ans << endl;
	}
	return 0;
}

