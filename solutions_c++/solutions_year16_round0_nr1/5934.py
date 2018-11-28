#define _CRT_SECURE_NO_WARNINGS
#include<iostream>

using namespace std;

typedef unsigned long long i64;

bool digits[10];
int dcount = 0;

void clear_digits()
{
	for (int i = 0; i < 10; i++)
		digits[i] = false;
}

void update_digits(i64 number)
{
	while (number != 0)
	{
		i64 remaining = number % 10;
		if (!digits[remaining])
		{
			dcount++;
			digits[remaining] = true;
		}
		number /= 10;
	}
}

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		i64 number;
		cin >> number;
		if (number == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}

		i64 new_number = 0;
		while (dcount < 10)
		{
			new_number += number;
			update_digits(new_number);
		}
		printf("Case #%d: %d\n", i + 1, new_number);
		clear_digits();
		dcount = 0;
	}
	return 0;
}