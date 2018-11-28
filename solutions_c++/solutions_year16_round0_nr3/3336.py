#include <stdio.h>
#include <vector>
#include <string.h>
#include <string>
#include <chrono>
using namespace std;
using namespace std::chrono;

char input[105];
constexpr int N = 16;
constexpr int J = 50;
constexpr long long BEGIN = (1LL << (N - 1)) + 1;
constexpr long long END = 1LL << N;

bool notprime[10000000];
vector<int> primes;

void getprime()
{
	notprime[0] = notprime[1] = true;
	for (int i = 2; i < 10000000; i++)
	{
		if (notprime[i]) continue;
		primes.push_back(i);
		for (int j = 2; i * j < 10000000; j++)
		{
			notprime[j * i] = true;
		}
	}
}

bool isprime(long long foo)
{
	if (foo < 10000000) return !notprime[foo];
	for (int i = 0; i < primes.size(); i++)
	{
		if (foo % primes[i] == 0) return false;
		if (primes[i] * primes[i] > foo) return true;
	}
	return true;
}

bool test(long long foo)
{
	if (isprime(foo)) return false;
	char buf[100];
	_i64toa(foo, buf, 2);
	for (int i = 2; i <= 10; i++)
	{
		if (isprime(strtoll(buf, nullptr, i))) return false;
	}
	return true;
}

bool output(long long foo)
{
	char buf[100];
	_i64toa(foo, buf, 2);
	printf("%s ", buf);
	for (int i = 2; i <= 10; i++)
	{
		long long foo2 = strtoll(buf, nullptr, i);
		for (int i = 0; i < primes.size(); i++)
		{
			if (foo2 % primes[i] == 0)
			{
				printf("%d ", primes[i]);
				break;
			}
		}
	}
	return true;
}

int main()
{
	freopen("output.txt", "w", stdout);
	auto a = high_resolution_clock::now();
	getprime();
	auto b = high_resolution_clock::now() - a;
	fprintf(stderr, "%lld ms\n", duration_cast<milliseconds>(b).count());

	printf("Case #1:\n");

	int count = 0;
	for (long long b = BEGIN; b < END && count < J; b += 2)
	{
		if (test(b))
		{
			count++;
			output(b);
			printf("\n");
		}
	}
}