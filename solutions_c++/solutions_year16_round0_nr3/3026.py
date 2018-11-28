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
		printf("Case #%d:\n", t);

		int N, J;
		scanf("%d %d", &N, &J);

		ull_t mx = (1ll << N);

		ull_t s = (1ull << (N - 1)) | 1ull;

		set<ull_t> w;

		int j = 0;
		while (j < J)
		{
			vector<ull_t> d;

			do
			{
				++s;

				assert(s < mx);
			} while ((s & 1) == 0);

			ull_t q;

			for (int b = 2; b <= 10; b++)
			{
				ull_t q_b = 0;
				ull_t p_b = 1;
				q = s;

				while (q != 0)
				{
					q_b += p_b * (q & 1ull);
					p_b *= b;
					q >>= 1;
				}

				ull_t r = (ull_t)(sqrt(double(q_b)) + 1);

				for (int i = 0; i != primes.size() && primes[i] <= r; i++)
				{
					if (q_b % primes[i] == 0)
					{
						d.push_back(primes[i]);
						break;
					}
				}

				if (d.size() + 1 != b)
				{
					break;
				}
			}

			if (d.size() + 1 == 10)
			{
				ull_t q_binary = 0;

				ull_t q = s;
				ull_t p = 1;

				while (q != 0)
				{
					q_binary += p * (q & 1ull);
					p *= 10;
					q >>= 1;
				}

				printf("%llu", q_binary);

				for (int i = 0; i != d.size(); i++)
				{
					printf(" %llu", d[i]);
				}

				printf("\n");

				j++;
			}

			// s *= m;
		}
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
