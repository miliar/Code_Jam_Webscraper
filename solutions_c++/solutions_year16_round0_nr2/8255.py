#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int str_to_bit_state(char *str, int str_size)
{
	int res = 0;
	for (int i = 0; i < strlen(str); i++)
		if (str[i] == '+')
			res += (1 << i);
	return res;
}

int flip(int input_state, int layer, int str_size) // layer belong to [1, n]
{
	int remain = (((1 << str_size) - 1 - ((1 << layer) - 1)) & input_state);
	int turn_over = 0;
	for (int i = 0; i < layer; i++)
	{
		turn_over = (turn_over << 1);
		if (((input_state >> i) & 1) == 0)
			turn_over++;
	}
	return (remain + turn_over);
}

int q[2000], step[2000];
char input_str[200];
bool checked[2000];

int main()
{
	int test_case, top, tail;
	scanf("%d", &test_case);
	for (int case_cnt = 1; case_cnt <= test_case; case_cnt++)
	{
		scanf("%s", input_str);
		q[0] = str_to_bit_state(input_str, strlen(input_str));
		top = tail = step[0] = 0;
		for (int i = 0; i < (1 << strlen(input_str)); i++)
			checked[i] = false;
		checked[q[0]] = true;
		while (top <= tail)
		{
			int u = q[top];
			if (u == (1 << strlen(input_str)) - 1)
			{
				printf("Case #%d: %d\n", case_cnt, step[top]);
				break;
			}
			for (int i = 1; i <= strlen(input_str); i++)
			{
				int v = flip(u, i, strlen(input_str));
				if (!checked[v])
				{
					checked[v] = true;
					tail++;
					step[tail] = step[top] + 1;
					q[tail] = v;
				}
			}
			top++;
		}
	}
	return 0;
}







