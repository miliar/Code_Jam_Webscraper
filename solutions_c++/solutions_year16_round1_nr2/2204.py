//============================================================================
// Name        : file.cpp
// Author      : Xutong Wang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int t, m = 0, info[100][50], n, counter[2500], odd[50], x;

void printarray()
{
	for (int i = 0; i < n; i++)
	{
		cout << odd[i] << " ";
	}
	cout << endl;
}

int main()
{
	cin >> t;
	while (m < t)
	{
		m++;
		//reset
		x = 0;
		for (int i = 0; i < 50; i++)
		{
			odd[i] = 0;
		}
		for (int i = 0; i < 2500; i++)
		{
			counter[i] = 0;
		}
		//end of reset
		cin >> n;
		for (int i = 0; i < (2*n)-1; i++)
		{
			for (int j = 0; j < n; j++) cin >> info[i][j];
		}
		for (int i = 0; i < (2*n)-1; i++)
		{
			for (int j = 0; j < n; j++)
			{
				counter[info[i][j]]++;
			}
		}
		for (int i = 0; i < 2500; i++)
		{
			if (counter[i]%2 != 0)
			{
				odd[x] = i;
				x++;
			}
		}
		sort(odd, odd+n);
		cout << "Case #" << m << ": ";
		printarray();
	}
	return 0;
}

































