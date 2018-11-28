#include<iostream>
#include<stdio.h>
#pragma warning(disable:4996)

int Data[1005];
	
int main()
{
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int TT;
	int N;
	int Sum;
	int Ans;
	fscanf(in,"%d", &TT);	


	for (int t = 1; t <= TT;t++)
	{
		Sum = 0;
		Ans = 0;
		fscanf(in, "%d", &N);
		for (int i = 0; i <= N; i++)
		{
			fscanf(in, "%1d", &Data[i]);
			if (Sum < i)
			{
				Ans += i - Sum;
				Sum = i;	
			}
			Sum += Data[i];
		}
		fprintf(out, "Case #%d: %d\n", t, Ans);
	}
	return 0;
}