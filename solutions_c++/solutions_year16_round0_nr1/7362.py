//#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.out", "w", stdout);
	FILE *file;
	file = fopen("A-large.in", "r");
	int n = 0, p = 0;
	fscanf(file, "%d", &n);
	while (fscanf(file, "%d", &n) == 1)
	{
		p++;
		int sean[10] = { 11,11,11,11,11,11,11,11,11,11 }, flag = 0, now = n, j = 0, count = 0, temp = 0, multi = 1;
		do
		{
			do
			{
				flag = 0;
				temp = now % 10;
				now = (now - temp) / 10;
				for (int i = 0; i < 10; i++)
				{
					if (temp == sean[i])
					{
						flag++;
					}
				}
				if (flag == 0)
				{
					sean[j] = temp;
					j++;
				}
				if (j == 10)
				{
					break;
				}
			} while (now != 0);
			multi++;
			now = n*multi;
			count++;
			if (j == 10)
			{
				break;
			}
			else if (count == 999)
			{
				break;
			}
		} while (1);
		if (j == 10)
		{
			printf("Case #%d: %d\n",p, now - n);
		}
		else
		{
			printf("Case #%d: INSOMNIA\n",p);
		}
	}

	return 0;
}