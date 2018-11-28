#include <cstdio>
#include <cstdlib>

bool Found(int hist[])
{
	bool match = true;
	for(int i=0; i<10; ++i)
	{
		if(hist[i]!=0)
		{
			match = match && true;
		}
		else
		{
			match = match && false;
		}
	}
	return match;
}

void GetDigits(long long int N, int hist[])
{
	while(N/10 != 0)
	{
		hist[N%10]++;
		N = N/10;
	}
	hist[N%10]++;
}

long long int FindLastNumber(long int N)
{
	long long int num = N;
	if(N==0)
	{
		return 0;
	}
	int *hist = new int[10];
	for(int i=0; i<10; ++i)
	{
		hist[i] = 0;
	}
	GetDigits(num, hist);
	while(!Found(hist))
	{
		num += N;
		GetDigits(num, hist);
	}
	delete[] hist;
	return num;
}

int main()
{
	int Test;
	long int N;
	scanf("%d", &Test);
	long long int *lastNum = new long long int[Test];
	for(int t=0; t<Test; ++t)
	{
		scanf("%d", &N);
		lastNum[t] = FindLastNumber(N);
	}
	for(int t=0; t<Test; ++t)
	{
		if(lastNum[t]==0) {
			printf("Case #%d: INSOMNIA\n", t+1);
		}
		else {
			printf("Case #%d: %lli\n", t+1, lastNum[t]);
		}
	}
	delete[] lastNum;
	return 0;
}