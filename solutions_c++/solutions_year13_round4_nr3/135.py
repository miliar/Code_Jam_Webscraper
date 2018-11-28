#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <math.h>
#include <memory.h>

#define MAX 20

int A[MAX];
int B[MAX];
int N;

bool used[MAX];
int mas[MAX];
int right[MAX];
int left[MAX];

bool f(int step)
{
	if (step == N)
	{
		for (int i = 0; i < N; i++)
			left[i] = 1;
		for (int i = N - 1; i >= 0; i--)
			for (int j = i + 1; j < N; j++)
				if (mas[i] > mas[j] && left[i] < left[j] + 1)
					left[i] = left[j] + 1;
		for (int i = 0; i < N; i++)
			if (left[i] != B[i])
				return false;
		return true;
	}
	else
	{
		for (int i = 0; i < N; i++)
			if (!used[i])
			{
				int s = 1;
				for (int j = 0; j < step; j++)
					if (i > mas[j] && s < A[j] + 1)
						s = A[j] + 1;
				if (s == A[step])
				{
					mas[step] = i;
					used[i] = true;
					if (f(step + 1))
						return true;
					used[i] = false;
				}
			}
		return false;
	}
}


int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", &A[i]);
		for (int i = 0; i < N; i++)
			scanf("%d", &B[i]);
		for (int i = 0; i < N; i++)
			used[i] = false;
		f(0);
		printf("Case #%d:", t+1);
		for (int i = 0; i < N; i++)
			printf(" %d", mas[i] + 1);
		printf("\n");
	}

	return 0;
}