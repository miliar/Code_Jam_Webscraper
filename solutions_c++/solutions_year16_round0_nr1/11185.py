#include <cstdio>
#include <iostream>
#include <string.h>

using namespace std;

int n, t;
int map[11];
FILE *fp;
FILE *fp_r;
int check()
{
	for (int i = 0; i <= 9; i++){
		if (map[i] == 0){
			return 0;
		}
	}
	return 1;
}

void algo()
{
	if (n == 0){
		fprintf(fp,"INSOMNIA\n");
		return;
	}

	memset(map, 0, sizeof(map));
	unsigned long long sum = n;
	unsigned long long temp;
	while (1)
	{
		temp = sum;
		while (temp)
		{
			map[temp % 10] = 1;
			temp /= 10;
		}
		if (check())
		{
			fprintf(fp,"%lld\n", sum);
			break;
		}
		sum += n;
	}
}

int main()
{
	fp_r = fopen("A-large.in", "r");
	fp = fopen("Counting Sheep.txt", "w");
	fscanf(fp_r, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fprintf(fp, "Case #%d: ", i);
		fscanf(fp_r, "%d", &n);
		algo();
	}
	fclose(fp);
	return 0;
}