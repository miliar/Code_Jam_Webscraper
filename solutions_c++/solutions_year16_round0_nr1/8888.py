#include <iostream>

using namespace std;

unsigned long long checkDigits(unsigned long long n, unsigned &map)
{
	while(n != 0)
	{
		unsigned long long d = n % 10;
		map |= 1 << d;
		n /= 10;
	}

	if((map & 0x03ff) == 0x03ff)
		return true;

	return false;
}

unsigned long long checkN(unsigned long long N)
{
	unsigned map;
	unsigned long long n;

	if(N == 0)
		return 0;

	for(map = 0, n = N; checkDigits(n, map) == false; n += N);

	return n;
}

void readFromStdin()
{
	int T;

	cin >> T;

	for(int t = 0; t < T; t++)
	{
		unsigned long long N, result;
		cin >> N;

		cout << "Case #" << t+1 << ": ";
		
		if(result = checkN(N))
			cout << result;
		else
			cout << "INSOMNIA";

		cout << endl;
	}
}

int main()
{
	readFromStdin();
	return 0;
}
