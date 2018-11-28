#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdlib>

using namespace std;

const int SZ = 1001;

int num[SZ];

int my_judge(int x)
{
	if (x >= 1000) return 0;
	else if (x >= 100)
	{
		if((x / 100) != (x % 10)) return 0;
	}
	else if (x >= 10)
	{
		if ((x / 10) != (x % 10)) return 0;
	}
	int y = (int)sqrt(double(x));
	if (y * y != x) return 0;

	if (y >= 10)
	{
		if ((y / 10) != (y % 10)) return 0;
	}
	return 1;
}



int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, t;
	int i, j;
	scanf("%d", &T);
	memset(num, 0, sizeof(num));
	for (i = 1; i < SZ; i++)
	{
		if (my_judge(i))
			num[i] = num[i - 1] + 1;
		else
			num[i] = num[i - 1];
	}
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int A, B;
		scanf("%d%d", &A, &B);
		printf("%d\n", num[B] - num[A - 1]);
	}
	
	return 0;
}