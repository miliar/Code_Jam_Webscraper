#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	freopen("B-large.out", "w", stdout);
	FILE *file;
	file = fopen("B-large.in", "r");
	char *now, *done, all[200] = {};
	int p = 0;
	fgets(all, 200, file);
	while (p < 100)
	{
		fgets(all, 200, file);
		p++;
		int answer = 0;
		do
		{
			if (all[0] == '-')
			{
				done = strrchr(all, '-');
				now = all;
				while (now <= done)
				{
					char temp;
					temp = *now;
					*now = *done;
					*done = temp;
					if (*now == '+')
					{
						*now = '-';
					}
					else
					{
						*now = '+';
					}
					if (done != now)
					{
						if (*done == '+')
						{
							*done = '-';
						}
						else
						{
							*done = '+';
						}
					}
					now++;
					done--;
				}
				answer++;
			}
			else
			{
				if (strchr(all, '-') != NULL)
				{
					done = strchr(all, '-');
					done--;
					while (done >= all)
					{
						*done = '-';
						done--;
					}
					answer++;
				}
			}
		} while (strchr(all, '-') != NULL);
		printf("Case #%d: %d\n", p, answer);
	}

	return 0;
}