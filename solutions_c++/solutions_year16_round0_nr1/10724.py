#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

int n, m;

int numdigits(int number)
{
	int digits = 0;
	if (number < 0) digits = 1; // remove this line if '-' counts as a digit
	while (number) {
		number /= 10;
		digits++;
	}
	return digits;
}

int getdigit(int num, int place)
{
	int buff;
	buff = (num % (int)pow(10, place)) / (pow(10, place - 1));
	return buff;
}

int isfull(int arr[]) 
{
	int ind;
	for (ind = 0; ind < 10; ind++)
	{
		if (arr[ind] <= 0)
			return 0;
	}
	return 1;
}

int main()
{
	int i, j, k, t, tt, num, mul, val;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d\n", &tt);
	for (t = 1; t <= tt; ++t)
	{
		if (t > 1)
		{
			printf("\n");
		}

		scanf("%d\n", &val);
		if (val == 0) {
			printf("Case #%d: INSOMNIA", t);
			continue;
		}

		int dict[10] = {0,0,0,0,0,0,0,0,0,0};
		int mul = 1;
		while (!isfull(dict))
		{
			num = val * mul++;
			int len = numdigits(num);
			for (n = 0; n < len; n++) {
				dict[getdigit(num, n + 1)] = 1;
			}
		}
		printf("Case #%d: %d", t, num);
	}

	return 0;
}
