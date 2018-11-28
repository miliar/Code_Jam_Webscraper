// Problem A. Magic Trick.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	FILE *fp1;
	fp1 = fopen("d:\\out.txt","w");
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		int ta, tb, lista[16], listb[16];
		scanf("%d", &ta);
		for (int j = 0; j < 16; ++j)
			scanf("%d", &lista[j]);
		scanf("%d", &tb);
		for (int j = 0; j < 16; ++j)
			scanf("%d", &listb[j]);
		int mynum = 0, count = 0;
		for (int j = ta * 4 - 4; j < ta * 4; ++j)
		{
			for (int k = tb * 4 - 4; k < tb * 4; ++k)
			{
				if (lista[j] == listb[k])
				{
					mynum = lista[j];
					count++;
				}
			}
		}
		if(count == 0) fprintf(fp1, "Case #%d: Volunteer cheated!\n", i + 1);
		if(count == 1) fprintf(fp1, "Case #%d: %d\n", i + 1, mynum);
		if(count > 1) fprintf(fp1, "Case #%d: Bad magician!\n", i + 1);
	}
	fclose(fp1); 
	getchar();
	getchar();
	return 0;
}

