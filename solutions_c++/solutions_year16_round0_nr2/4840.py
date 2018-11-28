// GoogleSheep.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace System;

void doCase(char* str, int strlen, int caseNum)
{
	char cur = str[0];
	int total = 0;
	for (int i = 1; i < strlen; i++) {
		if (cur != str[i])
		{
			total++;
		}
		cur = str[i];
	}

	printf("Case #%d: %d\n", caseNum, total);
}


int main(array<System::String ^> ^args)
{
	FILE * fp;
	char buf[1000];
	size_t len = 0;
	size_t read;

	fp = fopen("C:\\Users\\Aaron\\Desktop\\input.txt", "r");

	long numTestCases = 0;
	fscanf(fp, "%d", &numTestCases);

	for (long i = 1; i < numTestCases+1; i++) {
		char str[101] = { 0 };
		fscanf(fp, "%s", str);
		int len = strlen(str);
		str[len] = '+';
		doCase(str, len+1, i);
	}

	int wait = 0;
	scanf("%d", &wait);

    return 0;
}
