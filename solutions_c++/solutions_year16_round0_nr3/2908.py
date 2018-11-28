#include <cstdio>
#include <cstring>
#include <vector>

const int N = 100000000;
int divisor[N];
std::vector<int> primes;


void prepare()
{
	for(int i = 2; i < N; i++)
		if(divisor[i] == 0)
		{
			primes.push_back(i);
			for(int j = i + i; j < N; j += i)
				if(divisor[j] == 0)
					divisor[j] = i;
		}
}


long long testPrime(long long x)
{
	if(x < N)
		return divisor[x];
		
	for(int i = 0; i < (int)primes.size(); i++)
	{
		int p = primes[i];
		if(x % p == 0)
			return p;
	}
	
	return 0;
}



void printMask(const long long mask, const int n)
{
	for(int i = 0; i < n; i++)
		printf("%lli", (mask >> (n - 1 - i)) & 1);
}

long long number(long long mask, long long base, const int n)
{
	long long r = 0;
	for(int i = 0; i < n; i++)
		r = (r * base) + ((mask >> (n - 1 - i)) & 1);

	return r;
}

void generate(int n, int r)
{
	printf("Case #1:\n");

	long long muls[11];

	const long long extra = (1LL << (n - 1)) | 1;
	const long long border = 1LL << (n - 2);
	for(long long pre = 0; pre < border && r > 0; pre++)
	{
		const long long mask = (pre << 1) | extra;


		bool ok = true;
		for(int i = 2; i <= 10; i++)
		{
			muls[i] = testPrime(number(mask, i, n));
			if(muls[i] == 0)
				ok = false;
		}

		if(!ok)
			continue;
			
		printMask(mask, n);
		for(int i = 2; i <= 10; i++)
			printf(" %lli", muls[i]);
		//	printf(" %lli (%lli)", number(mask, i, n), muls[i]);

		printf("\n");
		r--;
	}
	
	if(r > 0)
		printf("FAIL!!!");
}

int main()
{
	prepare();	
	generate(16, 50);
	return 0;
}

