// GoogleCodeJam1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<stdio.h>
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin, *fout;
	char input[2000];
	int test;
	int s_max;
	fopen_s(&fin,"D:\\A-large.in", "r");
	fopen_s(&fout,"data3.out", "w");
	fscanf_s(fin,"%d", &test,40);
	printf("%d", test);
	for (int j = 0; j != test; ++j){
		fscanf_s(fin,"%d", &s_max, 40);

		fscanf_s(fin,"%s", input, 2000);
		int number[2000];
		int i;

		for (i = 0; input[i]; ++i)
		{
			number[i] = input[i] - '0';
		}
		int sum = 0; int request = 0;
		for (int i = 0;i<=s_max; ++i)
		{
			if (number[i] == 0) continue;
			if (sum < i) {
				request += i - sum;
				sum = i;
			}
			sum += number[i];
		}
		fprintf(fout,"Case #%d: %d\n",j+1, request);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

