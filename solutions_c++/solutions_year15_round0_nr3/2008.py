#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

char s[1050];
char sign[500][500];
char mult[500][500];
char res[10500][10500];
char sgn[10500][10500];

void solve(int t)
{
	int n, x;
	scanf("%d%d", &n, &x);
	scanf("%s", s);
	for (int i = 1; i < x; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			s[i*n + j] = s[j];
		}
	}
	int l = n*x;
	s[l] = 0;
	for (int i = 0; i < l; ++i)
	{
		res[i][i + 1] = s[i];
		sgn[i][i + 1] = 1;
	}
	for (int i = 0; i < l; ++i)
	{
		for (int j = i + 2; j <= l; ++j)
		{
			res[i][j] = mult[res[i][j - 1]][s[j - 1]];
			sgn[i][j] = sign[res[i][j - 1]][s[j - 1]] * sgn[i][j - 1];
		}
	}
	bool ok = false;
	for (int i = 0; i < l; ++i)
	{
		for (int j = i + 1; j < l; ++j)
		{
			if (res[0][i + 1] == 'i' && sgn[0][i + 1] == 1 &&
				res[i + 1][j + 1] == 'j' && sgn[i + 1][j + 1] == 1 &&
				res[j + 1][l] == 'k' && sgn[j + 1][l] == 1)
			{
				ok = true;
			}
		}
	}
	printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	memset(sign, 1, sizeof(sign));
	mult['1']['1'] = '1';
	mult['1']['i'] = 'i';
	mult['1']['j'] = 'j';
	mult['1']['k'] = 'k';

	mult['i']['1'] = 'i';
	mult['i']['i'] = '1';
	sign['i']['i'] = -1;
	mult['i']['j'] = 'k';
	mult['i']['k'] = 'j';
	sign['i']['k'] = -1;

	mult['j']['1'] = 'j';
	mult['j']['i'] = 'k';
	sign['j']['i'] = -1;
	mult['j']['j'] = '1';
	sign['j']['j'] = -1;
	mult['j']['k'] = 'i';

	mult['k']['1'] = 'k';
	mult['k']['i'] = 'j';
	mult['k']['j'] = 'i';
	sign['k']['j'] = -1;
	mult['k']['k'] = '1';
	sign['k']['k'] = -1;

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		solve(i + 1);
	}
	return 0;
}