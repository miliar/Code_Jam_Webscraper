#define  _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

char input[200];

void print(int idx, int n)
{
	printf("Case #%d: %d\n", idx, n);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		scanf("%s", input);
		int len = strlen(input);
		int sum = 0;
		int idx = 0;
		bool first = true;
		while (idx < len)
		{
			if (input[idx] == '+')
			{
				first = false;
				while (input[idx] == '+') idx++;
			}
			if (input[idx] == '-')
			{
				if (first) sum++;
				else sum += 2;
				while (input[idx] == '-') idx++;
			}
		}
		print(cases, sum);
	}
	return 0;
}