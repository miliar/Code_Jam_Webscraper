// GoogleSheep.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace System;

int primes[1000000] = { 0 };

long long toBase10(long long num, long long base)
{
	long long result = 0;

	long long mult = 1;
	while (num > 0) {
		int mod = num % 10;
		result += mod * mult;
		mult *= base;
		num /= 10;
	}
	return result;
}

long long toBaseFromBase(long long num, long long toBase, long long fromBase) {
	long long result = 0;

	long long mult = 1;
	while (num > 0) {
		int mod = num % toBase;
		result += mod * mult;
		mult *= fromBase;
		num /= toBase;
	}
	return result;
}

long long primeDivisor(long long num)
{
	if (num <= 2) return num;
	if (num % 2 == 0) return 2;
	for (long long i = 3; i <= sqrt(num); i += 2)
	{
		if (num % i == 0)
			return i;
	}
	return num;
}

void doCase(int N, int J, int caseNum)
{
	printf("Case #%d:\n", caseNum);

	long long result = 0;

	long long NBegin = 1;
	long long NEnd = 1;

	for (long long i = 0; i < N; i++) {
		NEnd *= 2;
	}
	NBegin = NEnd / 2;

	int coinsFound = 0;

	for (long long i = NBegin; i < NEnd; i++) {
		long long reps[9] = { 0 };
		long long jam = toBaseFromBase(i, 2, 10);
		if (jam % 2 == 0) {
			continue;
		}
		bool isJam = true;
		for (long long base = 0; base < 9; base++) {
			reps[base] = toBaseFromBase(jam, 10, base + 2);

			long long div = primeDivisor(reps[base]);
			if (div == reps[base]) {
				isJam = false;
				break;
			}
			reps[base] = div;
		}
		if (isJam) {
			coinsFound++;
			printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", jam, reps[0], reps[1], reps[2], reps[3], reps[4], reps[5], reps[6], reps[7], reps[8]);

			if (coinsFound == J) {
				return;
			}

		}
	}
}


int main(array<System::String ^> ^args)
{
	FILE * fp;
	char buf[1000];
	size_t len = 0;
	size_t read;

	FILE * fp2;

	fp = fopen("C:\\Users\\Aaron\\Desktop\\input.txt", "r");
	fp2 = fopen("C:\\Users\\Aaron\\Desktop\\primes.txt", "r");

	long numTestCases = 0;
	fscanf(fp, "%d", &numTestCases);

	for (int i = 0; i < 1000000; i++) {
		fscanf(fp2, "%d", &(primes[i]));
	}


	for (long i = 1; i < numTestCases+1; i++) {
		int N = 0;
		int J = 0;
		fscanf(fp, "%d %d", &N, &J);
		doCase(N, J, i);
	}

	printf("DONE\n");

	int wait = 0;
	scanf("%d", &wait);

    return 0;
}
