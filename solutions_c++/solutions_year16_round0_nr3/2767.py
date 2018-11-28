#include <stdio.h>
#include <math.h>
#include <algorithm>
#define maxn 202

using namespace std;

int digit[52];
FILE *fp, *fp2;
int N, J;
int divisor[10];
long long int num=0;

bool isPrime(long long int n)
{
	if (n < 4) return true;
	if ((n & 1) == 0) return false;
	long long int e = (int) sqrt((double)n);
	for (long long int i = 3; i <= e; i += 2)
		if (n%i == 0)
			return false;
	return true;
}

long long int powCal(int base, int power)
{
	long long int sum=1;
	if(power==0)
		return 1;
	
	for(int i=1;i<=power;i++)
	{
		sum=sum*base;
	}
	return sum;
}

bool JamCoin()
{
	for(int b=2;b<=10;b++)
	{
		num=0;
		for(int i=0;i<N;i++)
		{
			if(digit[i]==1)
				num+=powCal(b, i);
		}
		if(isPrime(num))
			return false;
		else
		{
			for(long long int j=2;j<num;j++)
			{
				if(num%j==0)
				{
					divisor[b-2]=j;
					break;
				}
			} 
		}
	}
	return true;
}

void check(int posi)
{
	digit[posi]=1;
	if(J>0 && posi+1<N-1)
		check(posi+1);
	
	if(J>0 && posi+1==N-1 && JamCoin())
	{
		for(int i=N-1;i>=0;i--)
			fprintf(fp2, "%d", digit[i]);
		for(int i=0;i<9;i++)
		{
			fprintf(fp2, " %d", divisor[i]);
		}
		fprintf(fp2, "\n");
		J--;
	}

	digit[posi]=0;
	if(J>0 && posi+1<N-1)
		check(posi+1);	
	
	if(J>0 && posi+1==N-1 && JamCoin())
	{
		for(int i=N-1;i>=0;i--)
			fprintf(fp2, "%d", digit[i]);
		for(int i=0;i<9;i++)
		{
			fprintf(fp2, " %d", divisor[i]);
		}
		fprintf(fp2, "\n");
		J--;
	}
}

int main()
{
	fp = fopen("C-small-attempt2.in", "r");
	fp2 = fopen("Coutput.txt", "w");
	int test_case;
	fscanf(fp, "%d", &test_case);
	for(int i=1;i<=test_case; i++)
	{
		fprintf(fp2, "Case #%d:\n", i);
		fscanf(fp, "%d %d", &N, &J);
		for(int j=0;j<N;j++)
			digit[j]=0;
		digit[0]=1;
		digit[N-1]=1;
		check(1);
	}
	
	fclose(fp);
	fclose(fp2);
	return 0;
}
