#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>

using namespace std;

int casos, c;
int res;
char cad[110];
int main()
{
	//*
	freopen("B-large.in", "r", stdin);
	freopen("Output.txt", "w", stdout);
	//*/
	scanf("%d", &casos );
	while (casos--)
	{
		res = 0;
		scanf("%s", cad);
		if (cad[0] == '-')
			res++;
		char aux = cad[0];
		for (int i = 1; i < strlen(cad); i++)
		{
			if (cad[i] != aux)
				if (cad[i] == '-')
					res += 2;
			aux = cad[i];
		}
		
		printf("Case #%d: %d\n",++c, res);
	}
}
