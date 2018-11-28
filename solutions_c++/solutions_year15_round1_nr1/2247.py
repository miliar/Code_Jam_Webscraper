#include <stdio.h>
#include <string.h>
#include <math.h>

FILE *in = fopen("A-large.in", "rb");
FILE *out = fopen("output.txt", "w");
int t;
int n;
int result1=0;
int result2=0;
int arr[10002] = { NULL };
int a[10002] = { NULL };
int b[10002] = { NULL };


void input();
void process();

int main(void)
{
	input();
	return 0;
}

void input()
{
	int k;
	int i;
	int j;
	
	fscanf(in,"%d", &t);
	for (k = 1; k <= t; k++) {
		result1 = 0;
		result2 = 0;
		for (i = 1; i <= 10000; i++)
		{
			arr[i] = 0;
			a[i] = 0;
			b[i] = 0;
		}
		fscanf(in,"%d", &n);
		for (i = 1; i <= n; i++)
		{
			fscanf(in,"%d", &arr[i]);
		}
		process();
		fprintf(out, "Case #%d: %d %d\n", k, result1, result2);
	}
}

void process()
{
	int i;
	int max = 0;
	for (i = 1; i < n; i++)
	{
		if (arr[i] > arr[i + 1])
		{
			a[i] = arr[i] - arr[i + 1];
		}
	}
	for (i = 1; i < n; i++)
	{
		if (max < arr[i] - arr[i + 1])
		{
			max = arr[i] - arr[i + 1];
		}
	}
	for (i = 1; i < n; i++)
	{
		if (max > arr[i])
		{
			b[i] = arr[i];
		}
		else
		{
			b[i] = max;
		}
	}
	for (i = 1; i < n; i++)
	{
		result1 = result1 + a[i];
		result2 = result2 + b[i];
	}
}