//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

int a[2000];
string st;
int main()
{
	freopen("A.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int smax;
	for (int c = 1; c <= T; ++c)
	{
		cin >> smax;
		cin >> st;
		int ans = 0;
		int total = 0;
		for (int i = 0; i <= smax; ++i)
		{
			int t = st[i] - '0';
			if (total < i)
			{
				ans += i - total;
				total = i;
			}
			total += t;
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}
