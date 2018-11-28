#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool finish(char* buf)
{
	for (int i = 0; buf[i]; i++)
	{
		if (buf[i] == '-')
		{
			return false;
		}
	}
	return true;
}

void flip(char buf[], int end)
{
	char tbuf[1000] = { 0, };
	int p = 0;

	for (int i = 0; i < end; i++)
	{
		if (buf[i] == '+')
		{
			buf[i] = '-';
		}
		else
		{
			buf[i] = '+';
		}
		tbuf[p++] = buf[i];
	}
	strrev(tbuf);
	strncpy(buf, tbuf, end);
}

void doit(char* buf)
{
	char s = buf[0];
	int i = 1;

	if (s == '+')
	{
		for (; buf[i]; i++)
		{
			if (buf[i] == '-')
			{
				break;
			}
		}
	}
	else
	{
		for (; buf[i]; i++)
		{
			if (buf[i] == '+')
			{
				break;
			}
		}
	}
	flip(buf, i);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		char buf[1000] = { 0, };
		int count = 0;
		scanf("%s", buf);
		while (true)
		{
			if (finish(buf))
			{
				break;
			}
			doit(buf);
			count++;
		}
		printf("Case #%d: %d\n", i, count);
		fprintf(stderr,"Case #%d: %d\n", i, count);
	}
	return 0;
}