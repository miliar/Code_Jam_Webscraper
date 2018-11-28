#include <iostream>
#include <cstring>
using namespace std;
typedef unsigned long long ull;

void analyzeDigits(ull n, bool *digits)
{
	while (n > 0)
	{
		int d = n % 10;
		digits[d] = true;
		n /= 10;
	}
}

bool allDigitsSeen(bool *digits)
{
	bool res = true;
	for (int i = 0; i < 10; i++)
		res = res && digits[i];
	return res;
}

int main() 
{
	std::ios_base::sync_with_stdio(false);

	int numTestCases;
	scanf("%d", &numTestCases);

	for (int t = 0; t < numTestCases; t++) 
	{
		int m;
		scanf("%d", &m);
		ull n = m;

		if (m == 0)
		{
			printf("Case #%d: INSOMNIA\n", t+1);
			continue;
		}

		bool digits[10];
		memset(digits, false, 10 * sizeof(bool));

		int count = 0;
		while (!allDigitsSeen(digits))
		{
			count++;
			ull k = count * n;
			analyzeDigits(k, digits);
		}

		printf("Case #%d: %llu\n", t+1, count * n);
	}
	return 0;
}