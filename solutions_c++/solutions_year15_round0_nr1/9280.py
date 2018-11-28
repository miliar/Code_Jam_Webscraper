// Author: Hoang Duc Viet
#include <iostream>
#include <fstream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

#define PF printf
#define SF scanf

using namespace std;
typedef long long ll;
int itest = 1, ntest = 1;

int n;
char s[1010];

void _solve()
{
	int i, j;
	int k = strlen(s);
	int standing = 0;
	int res = 0;
	
	for (i=0; i<k; i++)
	{
		if (i <= standing)
		{
			standing += s[i]-'0';
		}
		else
		{
			res += i - standing;
			standing = i + s[i]-'0';
		}
	}
	
	PF("Case #%d: %d\n", itest, res);
}

void _input()
{
	int i, j;

	SF("%d %s", &n, s);
}

int main()
{
	#ifndef ONLINE_JUDGE
		#define FILE_IO "a"
		freopen(FILE_IO ".inp", "r", stdin);
		freopen(FILE_IO ".out", "w", stdout);
	#endif

	SF("%d", &ntest);
	for (itest=1; itest<=ntest; itest++)
	{
		_input();
		_solve();
	}

	return 0;
}

