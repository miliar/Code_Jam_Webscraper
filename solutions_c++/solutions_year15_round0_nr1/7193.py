#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

int main()
{
	char str[1000+10];
	int ans, sum;
	int T,smax;

	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d", &smax);
		scanf("%s", str);
		ans = sum = 0;

		for (int s=0; s<=smax; s++)
		{
			if (str[s] > '0')
			{
				if (sum >= s)
				{
					sum += str[s]-'0';
				}
				else
				{
					ans += s-sum;
					sum = s+str[s]-'0';
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
