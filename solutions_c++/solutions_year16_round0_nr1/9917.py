#include <stdio.h>

int testcase, index;
long long int N;
int mul;
int number[10];

int isDone(void);
void check(long long int n);

int main(void)
{
	FILE *in, *out;
	in = fopen("A-large.in", "r");
	out = fopen("counting_sheep_large.out", "w");

	fscanf(in, "%d", &testcase);
	for(index = 0; index<testcase; index++)
	{
		int i=0;
		long long int temp;
		mul = 1;
		for(i=0; i<10; i++)
			number[i] = 0;
		fscanf(in, "%lld",&N);

		if(N == 0)
			fprintf(out, "Case #%d: INSOMNIA\n", index+1);
		else
		{
			while(isDone() == 0)
			{
				temp = N*mul;
				check(temp);
				mul++;
			}
			fprintf(out, "Case #%d: %lld\n", index+1, temp);
		}
	}

	return 0;

}

int isDone(void)
{
	int i;
	int flag = 1;
	for(i=0; i<10; i++)
	{
		if(number[i] == 0)
			flag = 0;
	}

	return flag;
}

void check(long long int n)
{
	long long int temp = 0;
	int div = 10;
	while(1)
	{
		if(n == 0)
			break;
		temp = n%div;
		number[temp] = 1;
		n = n/div;
	}
}