#include <stdio.h>

int list[40], len;
long long int store[11][2];

int isPrime(int a)
{
	long long int i, w,x;
	x = store[a][0];
	if (x == 2 || x == 3)
		return 1;
	if (x % 2 == 0)
	{
		store[a][1] = 2;
		return 0;
	}
	if (x % 3 == 0)
	{
		store[a][1] = 3;
		return 0;
	}
	i = 5;
	w = 2;
	while (i*i <= x)
	{
		if (x%i == 0)
		{
			store[a][1] = i;
			return 0;
		}
		i += w;
		w = 6 - w;
	}
	return 1;
}

long long int cal(int base)
{
	long long int i, ans;
	ans = 0;
	i = 0;
	while (list[i] != 9)
		ans = ans*base + list[i++];
	return ans;
}

void add()
{
	int i;
	list[len - 2]++;
	for (i = len - 2;list[i] == 2;i--)
	{
		list[i] -= 2;
		list[i - 1]++;
	}
}

int main()
{
	int n, i;
	long long int num, j;
	num = 0LL;
	j = 0LL;
	FILE *fp_w, *fp_r;
	fp_w = fopen("CS_output.txt", "w");
	fp_r = fopen("C-small-attempt0.in", "r");

	fscanf(fp_r, "%d", &n);
	fscanf(fp_r, "%d %d", &len, &n);
	for (i = 0;i < 11;i++)
		for (j = 0;j < 2;j++)
			store[i][j] = 0LL;
	for (i = 0;i < 40;i++)
		list[i] = 9;
	fprintf(fp_w, "CASE #1:\n");
	list[0] = 1;
	for (i = 1;i < len - 1;i++)
		list[i] = 0;
	list[len - 1] = 1;

	while (n > 0)
	{
		for (i = 2;i <= 10;i++)
		{
			store[i][0] = cal(i);
			if (isPrime(i) == 1)
				break;
		}
		if (i != 11)
		{
			add();
			continue;
		}
		for (i = 0;list[i] != 9;i++)
			fprintf(fp_w, "%d", list[i]);
		for (i = 2;i <= 10;i++)
			fprintf(fp_w, " %lld", store[i][1]);
		
		fprintf(fp_w, "\n");
		add();
		n--;
	}

	fclose(fp_w);
	fclose(fp_r);
	return 0;
}