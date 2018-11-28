#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int N, J;
int arr[40];
int size;
long long ans[11];
int sizeA;

void convert(long long a)
{
	size = 0;
	while (a!=0)
	{
		long long r = a % 2;
		arr[size++] = r;
		a /= 2;
	}
}

long long ret(int base)
{
	long long retLL = 0;
	long long g = 1;
	for (int i = 0; i < size; ++i)
	{
		retLL += ((long long) arr[i] * g);
		g *= base;
	}
	return retLL;
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	int ts = 1;
	while (T--)
	{
		scanf("%d %d", &N, &J);
		printf("Case #%d: \n", ts++);

		long long standard = 1;
		
		for (int i = 0; i < N - 1; ++i)
			standard <<= 1;
		standard += 1;
		
		int cnt = 0;
		while (cnt!=J)
		{
			sizeA = 0;
			convert(standard);
			bool isAns = true;
			for (int base = 2; base <= 10; ++base)
			{
				long long tmp = ret(base);
				bool isPrime = true;
				for (long long i = 2; i <= sqrt(tmp); ++i)
				{
					if (tmp%i == 0){
						isPrime = false;
						ans[sizeA++] = i;
						break;
					}
				}
				if (isPrime)
				{
					isAns = false;
					break;
				}
			}

			if (isAns)
			{
				for (int i = size-1; i >=0; --i)
				{
					printf("%d", arr[i]);
				}
				for (int i = 0; i < sizeA; ++i)
				{
					printf(" %lld", ans[i]);
				}
				printf("\n");
				++cnt;
			}
			standard += 2;
		}


	}


}