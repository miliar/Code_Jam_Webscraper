#pragma warning(disable :4996)
#include<stdio.h>
#include<string.h>
using namespace std;
int c[12];
void count(long long int x)
{
	while (x > 0)
	{
		c[x % 10] = 1;
		x = x / 10;
	}
}
int check()
{
	for (int i = 0; i<= 9; i++)
	{
		if (c[i] == 1)
			continue;
		else
			return 0;
	}
	return 1;
}
void reset()
{
	for (int i = 0; i <= 9; i++)
	{
		c[i] = 0;
	}
}
int main(){
	int t, ans, sum;
	long long int n;

	FILE *f = fopen("A-large.in", "r");
	FILE *fo = fopen("out.txt", "w+");
	fscanf(f, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fscanf(f, "%lld", &n);
		if (n == 0)
		{
			fprintf(fo, "Case #%d: INSOMNIA\n", i);
		}
		else{
			reset();
			long long int a = 1;
			while (check() == 0)
			{
				count(a*n);
				a++;
			}
			fprintf(fo, "Case #%d: %lld\n", i, (a - 1)*n);
		}
	}
	return 0;
}