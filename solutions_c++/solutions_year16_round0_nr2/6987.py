//============================================================================
// Name        : panckaes.cpp
// Author      : Xutong Wang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int t, numarr[1000], prenum, c;
string pancakes;
char arr[1000];

void printarray(int*array)
{
	for (int i = 0; i < 100; i++)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}

int flips(string pancakes)
{
	prenum = 0, c = 0;
	for (int i = 0; i < 1000; i++)
	{
		arr[i] = 0;
		numarr[i] = 0;
	}
	strcpy(arr, pancakes.c_str());
	for (int i = 0; i < 1000; i++)
	{
		if (arr[i] == '+') numarr[i] = 1;
		else if (arr[i] == '-') numarr[i] = -1;
		else numarr[i] = 0;
	}
	//printarray(numarr);
	for (int i = 0; i < 1000; i++)
	{
		if (numarr[i] != prenum)
		{
			prenum = numarr[i];
			c++;
		}
		if (numarr[i+1] == 0)
		{
			if (numarr[i] == 1) c--;
			break;
		}
	}
	return c;
}

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> pancakes;
		cout << "Case #" << i+1 << ": ";
		cout << flips(pancakes) << endl;
	}
	return 0;
}
