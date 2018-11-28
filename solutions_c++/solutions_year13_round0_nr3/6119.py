#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<list>
using namespace std;

bool isOK(int x)
{
	if (x < 10)
	{
		return true;
	}
	else if (10 < x && x < 100)
	{
		if (x / 10 == x % 10)
		{
			return true;
		}
	}
	else if (100 <= x && x <= 1000)
	{
		if (x / 100 == x % 10)
		{
			return true;
		}
	}
	return false;
}
int main()
{

	 freopen("E:\\A.in", "r", stdin);
	 freopen("E:\\B.out", "w", stdout);
	int pf[101];
	int count = 0;
	for (int i = 1; i < 50; i++)
	{
		pf[count++] = i * i;
	}

	int T;
	scanf("%d", &T);
	for (int cas = 0; cas < T; cas++)
	{
		int num = 0;
		int A = 0, B = 0;
		scanf("%d %d", &A, &B);
		for (int i = 0; i < count && B >= pf[i]; i++)
		{
			if (A <= pf[i])
			{
				int temp = pf[i];

				if (isOK(temp) && isOK(i+1))
				{
					num++;
				}

			}
		}
		printf("Case #%d: %d\n", cas + 1, num);
	}

	return 0;
}
