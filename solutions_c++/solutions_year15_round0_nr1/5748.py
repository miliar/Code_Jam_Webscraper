#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <conio.h>

int calc(int shyMax, int* shyPpli);
int main()
{
	int loop, i, temp=0;
	FILE *fp;
	int Loop;
	int shyMax;
	char* shyPplc;
	int* shyPpli;
	int* result;

	fp = fopen("C:\\data\\google.txt", "rt");
	if (fp == NULL){ printf("open error!!\n"); getch();  return 0; }
	fscanf(fp, "%d\n", &Loop);
	result = (int*)calloc(sizeof(int), Loop);
	for (loop = 0; loop < Loop; loop++)
	{
		fflush(stdin);
		fscanf(fp, "%d\n", &shyMax);
	//	scanf("%d ", &shyMax);
		shyPplc = (char*)calloc(sizeof(char), shyMax + 1);
		shyPpli = (int*)calloc(sizeof(int), shyMax + 1);
		for (i = 0; i <= shyMax; i++)
		{
			if (i == shyMax - 1) fscanf(fp, "%c\n", &shyPplc[i]);
			else fscanf(fp, "%c", &shyPplc[i]);
		}
		for (i = 0; i < shyMax; i++)	shyPpli[i] = shyPplc[i] - '0';
		result[loop]=calc(shyMax, shyPpli);
		free(shyPplc);	free(shyPpli);
	}

	fp = fopen("C:\\data\\output.txt", "wt");
	for (loop = 0; loop < Loop; loop++)	fprintf(fp, "Case #%d: %d\n", loop+1, result[loop], "");
	free(result);
	fclose(fp);

	return 0;
}

int calc(int shyMax, int* shyPpli)
{
	int i, j=0;
	int audNum=0;
	int tempNum=0, temp=0;
	for (i = 1; i <= shyMax;i++)
	{
		temp += shyPpli[i-1]; // 이전 인원 더하기
		if (temp < i) tempNum = i - temp;
		if (tempNum > audNum) audNum = tempNum;
	}
	return audNum;
}
