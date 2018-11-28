// 2014rnd1c.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//#include <math.h>

using namespace std;

int GCD(long num1, long num2)
{
	long r;
	if( num1 < num2)
	{
		return GCD(num2, num1);
	}
	while((r = num1%num2) != 0)
		num1 = num2, num2 = r;
	return num2;
}

int cal1(long a, long b)
{
	int c = GCD(b, a);
	a /= c;
	b /= c;
	int n = 0;
	while (b%2 == 0)
	{
		b/=2;
		n++;
	}
	if (b != 1)
	{
		return -1;
	}
	double dA = a;
	while (dA >= 2.0)
	{
		dA /= 2.0;
		n--;
	}
	return n;
}


void main1()
{
	int nT = 0; 
	cin >> nT;
	for (int i = 0; i < nT; i++)
	{
		string str;
		cin >> str;
		int n = str.find('//');
		string strL = str.substr(0, n);
		string strR = str.substr(n+1, str.length()-n-1);

		long a = atoi(strL.c_str());
		long b = atoi(strR.c_str());

		int nR = cal1(a, b);

		cout << "Case #" << i+1 <<": ";
		if (nR < 1)
		{
			cout << "impossible" << endl;
		}
		else
		{
			cout << nR << endl;
		}
	}

}



int _tmain(int argc, _TCHAR* argv[])
{
	srand((unsigned)time(NULL));
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	main1();
	return 0;
}

