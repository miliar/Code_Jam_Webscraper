#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<iostream>
using namespace std;
bool ing(char *temp)
{
	for (int i = 0; i < strlen(temp); i++)
	{
		if (temp[i] == '-')
		{
			return true;
		}
	}
	return false;
}
int main()
{
	freopen("input.in", "r", stdin);
	FILE *f;
	f = fopen("out.txt", "w");
	int cas, k = 1;
	char temp[1000] = { 0, };
	scanf("%d", &cas);
	while (cas--)
	{
		int fl = 0;
		scanf("%s", temp);
		int length = strlen(temp);
		while (ing(temp))
		{
			int i = 0;
			if (temp[0] == '-')
			{
				for (; temp[i] != '+'; i++)
				{
					temp[i] = '+';
					if (i + 1 == length)
					{
						break;
					}
				}
			}
			else
			{
				for (; temp[i] != '-'; i++)
				{
					temp[i] = '-';
					if (i + 1 == length)
					{
						break;
					}
				}
			}
			fl++;
		}
		fprintf(f,"Case #%d: %d\n", k++, fl);
	}
}
