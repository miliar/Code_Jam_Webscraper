#include<stdio.h>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int Test;
	int T = 1;
	char box[2001];
	int temp[26];
	int num[10];
	int i;
	scanf("%d", &Test);
	while (T <= Test)
	{
		printf("Case #%d: ", T++);
		scanf("%s", &box);
		for (i = 0; i < 26; i++)
			temp[i] = 0;
		i = 0;
		while (box[i]!=0)
		{
			temp[box[i] - 65]++;
			i++;
		}
		for (i = 0; i < 10; i++)
			num[i] = 0;
		if (temp['Z' - 65] != 0)
		{
			num[0] = temp['Z' - 65];
			temp['Z' - 65] -= num[0];
			temp['E' - 65] -= num[0];
			temp['R' - 65] -= num[0];
			temp['O' - 65] -= num[0];
		}
		if (temp['W' - 65] != 0)
		{
			num[2] = temp['W' - 65];
			temp['T' - 65] -= num[2];
			temp['W' - 65] -= num[2];
			temp['O' - 65] -= num[2];
		}
		if (temp['U' - 65] != 0)
		{
			num[4] = temp['U' - 65];
			temp['F' - 65] -= num[4];
			temp['O' - 65] -= num[4];
			temp['U' - 65] -= num[4];
			temp['R' - 65] -= num[4];
		}
		if (temp['X' - 65] != 0)
		{
			num[6] = temp['X' - 65];
			temp['S' - 65] -= num[6];
			temp['I' - 65] -= num[6];
			temp['X' - 65] -= num[6];
		}
		if (temp['G' - 65] != 0)
		{
			num[8] = temp['G' - 65];
			temp['E' - 65] -= num[8];
			temp['I' - 65] -= num[8];
			temp['G' - 65] -= num[8];
			temp['H' - 65] -= num[8];
			temp['T' - 65] -= num[8];
		}
		if (temp['O' - 65] != 0)
		{
			num[1] = temp['O' - 65];
			temp['O' - 65] -= num[1];
			temp['N' - 65] -= num[1];
			temp['E' - 65] -= num[1];
		}
		if (temp['F' - 65] != 0)
		{
			num[5] = temp['F' - 65];
			temp['F' - 65] -= num[5];
			temp['I' - 65] -= num[5];
			temp['V' - 65] -= num[5];
			temp['E' - 65] -= num[5];
		}
		if (temp['S' - 65] != 0)
		{
			num[7] = temp['S' - 65];
			temp['S' - 65] -= num[7];
			temp['E' - 65] -= num[7];
			temp['V' - 65] -= num[7];
			temp['E' - 65] -= num[7];
			temp['N' - 65] -= num[7];
		}
		if (temp['T' - 65] != 0)
		{
			num[3] = temp['T' - 65];
			temp['T' - 65] -= num[7];
			temp['H' - 65] -= num[7];
			temp['R' - 65] -= num[7];
			temp['E' - 65] -= num[7];
			temp['E' - 65] -= num[7];
		}
		if (temp['I' - 65] != 0)
		{
			num[9] = temp['I' - 65];
			temp['N' - 65] -= num[9];
			temp['I' - 65] -= num[9];
			temp['N' - 65] -= num[9];
			temp['E' - 65] -= num[9];
		}

		for (i = 0; i <= 9; i++)
		{
			while (num[i])
			{
				printf("%d", i);
				num[i]--;
			}
		}
		printf("\n");
	}
	return 0;
}