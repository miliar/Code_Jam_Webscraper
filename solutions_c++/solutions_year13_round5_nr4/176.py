#include <cstdio>
#include <map>
#include <cstring>

using namespace std;

double E(int k, int N)
{	
	int prev = 0;
	double res = 0.0;
	for (int i=0; i<N; i++)
	{
		if (k & (1 << i))
		{
			prev++;
			res += double(prev)/double(N);
		}
		else
		{
			prev = 0;
		}
	}
	return res;
}

map<pair<int, int>, double> EincBuf;

double Einc(int k, int N)
{
	if (k == (1 << N)-1)
		return 0.0;
	
	while (k & 1)
	{
		k = k >> 1 | (1 << (N-1));
	}
	
	if (EincBuf.count(make_pair(k,N)))
		return EincBuf[make_pair(k,N)];

	EincBuf[make_pair(k,N)] = double(N)-E(k,N);
	
	int prev = 0;
	for (int i=1; i<N; i++)
	{
		if (k & (1 << i))
		{
			prev++;
		}
		else
		{
			prev++;
			EincBuf[make_pair(k,N)] += double(prev)/double(N)*Einc(k|(1<<i),N);
			prev = 0;
		}
	}
	
	prev++;
	EincBuf[make_pair(k,N)] += double(prev)/double(N)*Einc(k | 1, N);
	
	return EincBuf[make_pair(k,N)];	
}


void init()
{
	for (int k=0; k<(1 << 20); k++)
	{
		for (int N=1; N<=20; N++)
		{
			Einc(k,N);
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i=0; i<T; i++)
	{
		int k = 0;
		char buffer[30];
		scanf("%s", buffer);
		
		for (int j=strlen(buffer)-1; j>=0; j--)
		{
			k <<= 1;
			if (buffer[j] == 'X')
				k += 1;
		}
		
		printf("Case #%d: %.10f\n", i+1, Einc(k,strlen(buffer)));
	}
	return 0;
}
