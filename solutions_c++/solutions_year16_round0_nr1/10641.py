#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main()
{
	int N;
	int i,j;
	int data;
	int A[10] = { 0, };
	int count = 0;
	int value;
	int num;
	int hundred = 100;

	FILE *in_file;
	FILE *out_file;
	in_file = fopen("A-large.in","r");
	out_file = fopen("a.txt","w");

	fscanf(in_file,"%d", &N);

	for (i = 1; i <= N; i++)
	{
		fscanf(in_file,"%d", &value);
		num = 1;
		count = 0;
		hundred = 100;
		while (hundred--)
		{
			if (value == 0)
				break;

			data = value * num;

			while (data>0)
			{
				A[data % 10]++;
				data /= 10;
			}

			for (j = 0; j < 10; j++)
			{
				if (A[j] > 0)
					count++;
			}

			if (count == 10)
				break;
			else
				count = 0;

			num++;

		}

		if (count == 0)
			fprintf(out_file,"Case #%d: INSOMNIA\n", i);
		else
			fprintf(out_file,"Case #%d: %d\n", i, value * num);

		for (j = 0; j < 10; j++)
		{
			A[j] = 0;
		}
	}

}