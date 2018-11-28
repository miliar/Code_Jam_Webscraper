#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

#define LARGE 1
#define SMALL 0

#define FILE LARGE
#if FILE == SMALL
#define IN_FILE "A-small-practice.in"
#else
//#define IN_FILE "A-large-practice.in"
#define IN_FILE "A-large.in"
#define OUT_FILE "A-large.out"
#endif

long int solve(long long n);

int main()
{
	int num_tc, cur_tc, result;
	long long N;

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	scanf("%d\n", &num_tc);	//number of test cases

	for (cur_tc = 0; cur_tc < num_tc; cur_tc++)
	{
		printf("Case #%d: ", cur_tc + 1);
		scanf("%lld\n", &N);	//number of coordinates

		result = solve(N);
		if (result == 0)
		{

			printf("%s\n", "INSOMNIA");
		}
		else
		{
			printf("%d\n", result);
		}
	}
}

long int solve(long long N)
{
	int flags, flags_prev, i, Nval;
	long long n;
	flags = 0;
	flags_prev = 0;
	i = 1;
 	Nval = N;
	if (Nval == 0)
	{
		flags = 0xFFF;
	}
	else
	{
		do {
			n = N;
			do {

				int digit = n % 10;
				//putchar('0' + digit);
				flags |= 1 << digit;
				n /= 10;
			} while (n > 0);

			//if (flags_prev == flags)		// if no new digits found

			flags_prev = flags;
			i++;
			N = Nval * i;

		} while ((flags != 0x3FF) && (flags != 0xFFF));
	}

	return N - Nval;
}