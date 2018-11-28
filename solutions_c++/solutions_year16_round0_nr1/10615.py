#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

bool Arrays[11] = { false };

void factorize(long long m)
{
	//printf("The number is %d\n", m);
	while (m)
	{
		Arrays[m % 10] = true;
		m /= 10;
	}
}

bool isOK()
{
	for (long long i = 0; i < 10; i++)
		if (Arrays[i] == false)
			return false;

	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	memset(Arrays, false, sizeof(Arrays));

	long long n;
	long long cases;
	long long testCase = 0;

	while (cin >> cases)
	{
		for (long long i = 0; i < cases; i++)
		{
			cin >> n;

			memset(Arrays, false, sizeof(Arrays));
			if (n == 0)
				printf("case #%lld: INSOMNIA\n", ++testCase);
			else
			{
				long long count = 1;
				while (isOK() == false)
				{
					factorize(count*n);
					count++;
				}

				printf("case #%lld: %lld\n", ++testCase, (count - 1)*n);

			}

			memset(Arrays, false, sizeof(Arrays));
		}
	}


}