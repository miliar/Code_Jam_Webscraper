#define _CRT_SECURE_NO_WARNINGS

#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

#define MAX_N 32

typedef unsigned long long ull_t;

int main(int argc, char* argv[])
{
	vector<ull_t> primes;

	primes.push_back(2);

	for (ull_t x = 3; x <= 100000; x += 2)
	{
		ull_t b = (ull_t)(sqrt(double(x)) + 1);

		bool is_prime = true;
		for (int i = 0; i != primes.size() && primes[i] <= b; i++)
		{
			if (x % primes[i] == 0)
			{
				is_prime = false;
				break;
			}
		}

		if (is_prime)
		{
			primes.push_back(x);
		}
	}

	freopen("in.txt", "rb", stdin);
	freopen("out.txt", "wb", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:", t);

		int K, C, S;

		scanf("%d %d %d", &K, &C, &S);

		for (int i = 1; i <= K; i++)
		{
			printf(" %d", i);
		}

		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
