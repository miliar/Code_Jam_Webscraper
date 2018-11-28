#include <iostream>

using namespace std;

long long N, K;
long long one = 1;
long long del[22];
long long num[55];

long long prime(long long n)
{
	if (n == 2)
		return -1;
	if (n % 2 == 0)
		return 2;
	for (long long i = 3; i * i <= n; i += 2)
	{
		if (n % i == 0)
			return i;
	}
	return -1;
}

bool check(long long n)
{
	for (long long i = 0; i < N; i++)
	{
		if ((n & (one << i)) == (one << i))
			num[i + 1] = 1;
		else
			num[i + 1] = 0;
	}
	if (num[1] == 0 || num[N] == 0)
		return false;
	for (long long i = 2; i <= 10; i++)
	{
		del[i] = 0;
		long long mn = 1;
		for (long long j = 1; j <= N; j++)
		{
			
			del[i] += mn * num[j];
			mn *= i;
		}
	}
	for (int i = 2; i <= 10; i++)
	{
		del[i] = prime(del[i]);
		if (del[i] == -1)
			return false;
	}
	return true;
}

void print(long long n)
{
	for (long long i = N - 1; i >= 0; i--)
		cout << ((n & (one << i)) == (one << i));
	return;
}

int main()
{
	//freopen("", "r", stdin);
	freopen("out-1.txt", "w", stdout);
	cin >> N >> N >> K;
	cout << "Case #1:" << endl;
	for (long long i = 0; i < (one << N); i++)
	{
		if (check(i))
		{
			print(i);
			for (int j = 2; j <= 10; j++)
				cout << ' ' << del[j];
			cout << endl;
			K--;
			if (K == 0)
				break;
		}
	}
	return 0;
}