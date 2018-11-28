//============================================================================
// Name        : Counting.cpp
// Author      : Xutong Wang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int n, x, y, reccheck, c;
int number[10];

void printarray(int*array)
{
	for (int i = 0; i < 10; i++)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}

void record(int b)
{
	reccheck = 0;
	while(b!=0)
	{
		number[b%10] = 1;
		b = (b-(b%10))/10;
	}
	//printarray(number);
	for (int i = 0; i < 10; i++)
	{
		if (number[i] == 1) reccheck++;
	}
}

int sheep(int a)
{
	reccheck = 0, c = 1;
	for (int i = 0; i < 10; i++) number[i] = 0;
	//printarray(number);
	while (reccheck != 10)
	{
		record(c*a);
		c++;
	}
	return c*a;
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x;
		cout << "Case #" << i+1 << ": ";
		if (x==0) cout << "INSOMNIA" << endl;
		else cout << sheep(x)-x << endl;
	}
	return 0;
}
