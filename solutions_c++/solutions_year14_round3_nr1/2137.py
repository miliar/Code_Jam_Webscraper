#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <iostream>
using namespace std;

int main ()
{
	int n, m, i, j, k, len, re, a, b, ca = 1, ans;
	char c;
	//freopen("A-small-attempt6.in", "r", stdin);
	//freopen("A-small-attempt6.out", "w", stdout);

	scanf("%d",&re);
	while(re--)
	{
		scanf("%d%c%d",&a,&c,&b);
		int dd = b;
		
		//if(dd % a == 0)
		//	dd /= a;

		while(dd % 2 == 0)
		{
			dd /= 2;
		}

		if(dd != 1)
		{
			printf("Case #%d: impossible\n",ca++);
		}
		else
		{
			k = 0;
			while(b > a)
			{
				b /= 2;
				k++;
			}
			printf("Case #%d: %d\n",ca++,k);
		}
	}
	return 0;
}