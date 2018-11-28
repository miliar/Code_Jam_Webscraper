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
	freopen("A-small-attempt0.in", "r", stdin);  
    freopen("A-small-attempt0.out", "w", stdout);  
	int ca = 1;
	int re, a[4][4], count, n, b[4], c[4];
	scanf("%d",&re);
	while(re--)
	{
		scanf("%d",&n);
		count = 0;
		for(int i = 0 ; i < 4 ; i ++)
		{
			for(int j = 0 ; j < 4 ; j ++)
			{
				scanf("%d",&a[i][j]);
				if(n == i + 1)
					b[j] = a[i][j];
			}
		}

		scanf("%d",&n);
		for(int i = 0 ; i < 4 ; i ++)
		{
			for(int j = 0 ; j < 4 ; j ++)
			{
				scanf("%d",&a[i][j]);
				if(n == i + 1)
					c[j] = a[i][j];
			}
		}

		int index;
		for(int i = 0 ; i < 4 ; i ++)
			for(int j = 0 ; j < 4 ; j ++)
				if(b[i] == c[j])
				{
					count ++;
					index = i;
				}

		if(count == 1)
			printf("Case #%d: %d\n",ca++,b[index]);
		else if (count == 0)
			printf("Case #%d: Volunteer cheated!\n",ca++);
		else
			printf("Case #%d: Bad magician!\n",ca++);
	}
	return 0;
}