// GoogleSheep.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

using namespace System;

FILE * fp2;

void doCase(long long N, int caseNum)
{
	bool numberSeen[10] = { false };
	if (N == 0)
	{
		printf("Case #%d: INSOMNIA\n", caseNum);
		return;
	}

	long long cnt = 1;
	while (1) {
		long long M = N*cnt;
		while (M > 0) {
			long long d = M % 10;
			numberSeen[d] = true;
			M = M / 10;

			bool done = true;
			for (int i = 0; i < 10; i++) {
				if (numberSeen[i] == false) {
					done = false;
					break;
				}
			}
			if (done) {
				printf("Case #%d: %d\n", caseNum, N*cnt);
				fprintf(fp2, "Case #%d: %d\n", caseNum, N*cnt);
				return;
			}
		}
		cnt++;
	}
}


int main(array<System::String ^> ^args)
{
	FILE * fp;
	char buf[1000];
	size_t len = 0;
	size_t read;

	fp = fopen("C:\\Users\\Aaron\\Desktop\\input.txt", "r");
	fp2 = fopen("C:\\Users\\Aaron\\Desktop\\output.txt", "w");

	long numTestCases = 0;
	fscanf(fp, "%d", &numTestCases);

	for (long i = 1; i < numTestCases+1; i++) {
		long num = 0;
		fscanf(fp, "%lld", &num);
		doCase(num, i);
	}

	int wait = 0;
	scanf("%d", &wait);

    return 0;
}
