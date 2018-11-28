// CodeJam2015.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

char s[10002];
int main(int argc, char* argv[])
{

	freopen("A-large.in", "r", stdin);
	freopen("ALarge.out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int n;
		cin >> n >> s;
		int res = 0;
		int cnt = 0;
		for (int i = 0; i <= n; ++i)
		{
			int val = s[i] - '0';
			if (val > 0 && cnt < i)
			{
				res += i - cnt;
				cnt = i;
			}
			cnt += val;
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}

