// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <assert.h>

int map[4][4] = { { 1, 2, 4, 8 }, { 2, -1, 8, -4 }, { 4, -8, -1, 2 }, { 8, 4, -2, -1 } };

int calcpos(int in){
	int i = 0;
	while ((in>>=1) > 0){
		i++;
	}
	return i;
}

int getLetter(int L, int X, int *a, long int p0, long int p1){
	long int i;
	int curVal = 0;
	int sign = 1;

	for (i = p0; i < p1; i++){
		curVal = map[calcpos(curVal)][calcpos(a[i%L])];
		if (curVal < 0){
			sign *= -1;
			curVal *= -1;
		}
	}
	return curVal*sign;
}

long int find_letter(int L, long int X, int *a, int l, int reverse, int *sign)
{
	int repmax = X;// X < 4 ? X : 4;
	int i, curVal = 0, curSign = 1;

	for (i = 0; i < repmax*L; i++){
		curVal = map[calcpos(curVal)][calcpos(a[i%L])];

		if (curVal < 0){
			curSign *= -1;
			curVal *= -1;
		}

		if (curVal == l){
			*sign = curSign;
			return i;
		}
	}
	return -1;
}
long int find_letter_reverse(int L, long int X, int *a, int l, int *sign)
{
	int repmax = X;
	int i, curVal = 0, curSign = 1;

	for (i = L*X - 1; i > -1; i--){
		curVal = map[calcpos(a[i%L])][calcpos(curVal)];
		if (curVal < 0){
			curSign *= -1;
			curVal *= -1;
		}

		if (curVal == l){
			*sign = curSign;
			return i;
		}
	}
}

void isCorrect(int L, long int X, int *a){
	long int pi, pk;
	int si, sk, l;

	pi = find_letter(L, X, a, 2, 0, &si);
	pk = find_letter_reverse(L, X, a, 8, &sk);

	l = getLetter(L, X, a, pi+1, pk);

	if ((l*si*sk) == 4)
		printf("Yes\n");
	else
		printf("No\n");
}

int calcVal(char in)
{
	if (in == 'i')
		return 2;
	else if (in == 'j')
		return 4;
	else if (in == 'k')
		return 8;
	assert(1);
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T, i;
	scanf_s("%d", &T);
	for (i = 0; i < T; i++){
		int L;
		long int X;
		char a[10001];
		int array[10001], j;
		scanf_s("%d %d", &L, &X, 1);
		scanf_s("%s", a, 10001);
		for (j = 0; j < L; j++){
			array[j] = calcVal(a[j]);
		}
		printf("Case #%d: ", i + 1);
		isCorrect(L, X, array);
	}
	return 0;
}

