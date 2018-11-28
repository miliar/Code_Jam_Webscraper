#include<stdio.h>

int box[26] = { 0, };
int N;
bool check(int num)
{
	if (num == 0)
		return true;
	int max = 0;
	for (int i = 0; i < N; i++)
	{
		if (box[i] > max)
			max = box[i];
	}
	
	if (max <= num / 2)
		return true;
	else
		return false;
}
void search(int num)
{
	int i, j;

	for (i = 0; i < N; i++)
	{
		if (box[i] > 0)
		{
			box[i]--;
			if (check(num - 1))
			{
				printf("%c ", i + 65);
				search(num - 1);
			}
			else
				box[i]++;
		}
	}
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
		{
			if (i == j)
			{
				if (box[i] > 1)
				{
					box[i]--;
					box[j]--;
					if (check(num - 2))
					{
						printf("%c%c ", i + 65, j + 65);
						search(num - 2);
					}
					else
					{
						box[i]++;
						box[j]++;
					}
				}
			}
			else
			{
				if (box[i] > 0 && box[j] > 0)
				{
					box[i]--;
					box[j]--;
					if (check(num - 2))
					{
						printf("%c%c ", i + 65, j + 65);
						search(num - 2);
					}
					else
					{
						box[i]++;
						box[j]++;
					}
				}
			}
		}
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int Test;
	int T = 1;
	int i;
	int sum = 0;
	scanf("%d", &Test);
	while (T <= Test)
	{
		printf("Case #%d: ", T);
		scanf("%d", &N);
		sum = 0;
		for (i = 0; i < N; i++)
		{
			scanf("%d", &box[i]);
			sum += box[i];
		}
		search(sum);
		printf("\n");
		T++;
	}
	return 0;
}