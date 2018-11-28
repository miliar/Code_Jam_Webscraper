#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

#define IN_FILE "A-large.in"
#define OUT_FILE "A-large.out"

#define MAX_S	1000

int solve(char* c, int size);

int main()
{
	int T, cur_tc, i, result;
	long long N;
	char c;
	char answer[MAX_S];
	char temp[MAX_S];
	char front;
	char back;
	c = 0, i = 0;


	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	scanf("%d\n", &T);	//number of test cases

	for (cur_tc = 0; cur_tc < T; cur_tc++)
	{
		printf("Case #%d: ", cur_tc + 1);
		do {
			result = scanf("%c", &c);
			if (result != -1)
			{
				if (i == 0)
				{
					//strcat(answer, &c);
					sprintf(temp, "%c", c);
					front = c;
					back = c;
				}
				else if (c == '\n')
				{
					i = 0; // eof do nothing
				}
				else if (c < front)
				{
					sprintf(temp, "%s%c", answer, c);
					back = c;
				}
				else
				{
					sprintf(temp, "%c%s", c, answer);
					front = c;
				}
				if (c != '\n')
				{
					strcpy(answer, temp);
				}
				i++;
			}
		} while (c != '\n' && result == 1);
		printf("%s\n", answer);
		i = 0;


	}
}

int solve(char* c, int size)
{

	return 0;
}