
#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <conio.h>
#include <stdio.h>
#include <string.h>

//#define IN_FILE_NAME "A-test-practice.in"
//#define OUT_FILE_NAME "A-test-practice.out"

#define IN_FILE_NAME "A-large.in"
#define OUT_FILE_NAME "A-large.out"

bool FillDigits(int arr[10], long long int N)
{
	while (N > 0)
	{
		int d = N % 10;
		arr[d]++;
		N /= 10;
	}
	for (int i = 0; i < 10; i++)
	{
		if (!arr[i])
			return false;
	}
	return true;
}

int main()
{
	freopen(IN_FILE_NAME, "r", stdin);
	freopen(OUT_FILE_NAME, "w", stdout);

	int t, tests;
	scanf("%d", &tests);

	for (t = 0; t < tests; t++)
	{
		long long int n;
		scanf("%lld", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t + 1);
			continue;
		}
		int arr[10];
		memset(arr, 0, sizeof(arr));

		long long int nr = n;
		while (!FillDigits(arr, nr))
		{
			nr += n;
		}

		printf("Case #%d: %lld\n", t+1, nr);
	}
}