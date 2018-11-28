#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;


unsigned long long getNumber(unsigned long long current, int base)
{
	unsigned long long s = 1;
	unsigned long long result = 0;
	char buf[100] = { 0, };
	//sprintf(buf, "%d", current);
	itoa(current, buf, 2);
	strrev(buf);
	for (int i = 0; buf[i]; i++)
	{
		if (buf[i] == '1')
		{
			result += 1 * s;
		}
		s *= base;
	}
	return result;
}

unsigned long long isprime(unsigned long long target)
{
	for (unsigned long long i = 2; i <= sqrt((double)target); i++)
	{
		if (target % i == 0)
		{
			return i;
		}
	}
	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int N, J;
		scanf("%d%d", &N, &J);

		int start = 1 << (N - 1);
		int end = 1 << N;
		start++;
		printf("Case #%d:\n", i);
		for (; start < end; start += 2)
		{
			vector<unsigned long long> ha;
			if (J == 0)
			{
				break;
			}
			for (int i = 2; i <= 10; i++)
			{
				unsigned long long mod = getNumber(start, i);

				unsigned long long val = isprime(mod);
				if (val == -1)
				{
					break;
				}
				else
				{
					ha.push_back(val);
				}
			}
			if (ha.size() == 9)
			{
				char buf[2000] = { 0, };
				itoa(start, buf, 2);
				printf("%s ", buf);
				for (int i = 0; i < ha.size(); i++)
				{
					printf("%d ", ha[i]);
				}
				printf("\n");
				J--;
			}
		}
	}
	return 0;
}