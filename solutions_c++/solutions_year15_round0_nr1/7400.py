// GoogleCodejamc++.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))
int main()
{
#ifdef _DEBUG
	freopen("d:\\A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif // _DEBUG
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		int kMax;
		scanf("%d ", &kMax);
		int nNeed = 0;
		int nSum = 0;
		char c;
		for (int k = 0; k <= kMax;k++)
		{
			scanf("%c", &c);
			if (nSum < k && c > '0')
			{
				nNeed = MAX(nNeed, k - nSum);
			}
			nSum += (c - '0');

		}
		scanf("\n");
		printf("Case #%d: %d\n", i + 1, nNeed);
	}
	return 0;
}

