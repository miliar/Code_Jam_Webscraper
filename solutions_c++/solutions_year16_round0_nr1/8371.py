#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>

using namespace std;

int n,casos,c,i,num[10];
int main()
{
	//*
	freopen("A-large.in", "r", stdin);
	freopen("Output.txt", "w", stdout);
	//*/
	scanf("%d", &casos );
	while (casos--)
	{
		for (int j = 0; j < 10; j++)
			num[j] = 1;

		scanf("%d", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ++c);
			continue;
		}
		for (i = n; ; i += n)
		{
			int aux=0;
			for (int j = 0; j < 10; j++)
			{
				aux += num[j];
				if (aux != 0)
					break;
			}
			if (aux == 0)
				break;
			for (aux = i; aux!=0;aux = aux / 10)
			{
				num[aux%10]=0;
			}
		}
		printf("Case #%d: %d\n",++c, i-n);
	}
}
