#include <iostream>
#include <bitset>

using namespace std;

typedef unsigned long long LargeInt;

int main()
{
	int T;
	cin >> T;
	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		bitset<10> foundDigits;
		int digitCount = 0;
		int N;
		cin >> N;
		
		cout << "Case #" << nTestCase << ": ";
		
		if (N == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}

		LargeInt currentN;
		for (currentN = N; digitCount < 10; currentN += N)
			for (LargeInt n = currentN; n > 0; n /= 10)
			{
				int digit = n % 10;
				if (!foundDigits[digit])
				{
					foundDigits[digit] = true;
					digitCount++;
				}
			}
		cout << (currentN - N) << endl;
	}

	return 0;
}