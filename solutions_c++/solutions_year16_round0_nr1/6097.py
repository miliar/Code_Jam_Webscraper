#include <iostream>
#include <vector>

using namespace std;

bool hasDigit(long long x, int d)
{
	while(x > 0)
	{
		int lx = x % 10;
		if(lx == d)
			return true;

		x /= 10;
	}
	return false;
}

long long getLastNumber(long long N)
{
	vector<bool> seenDigits(10);
	long long M = N;

	while(1)
	{	
		for(int i = 0; i < 10; i++)
		{
			if(hasDigit(M, i))
				seenDigits[i] = true;
		}

		bool done = true;
		for(int i = 0; i < 10; i++)
		{
			if(!seenDigits[i])
				done = false;
		}
		
		if(done)
			return M;
		else
			M += N;
	}
}

int main(void)
{
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";

		long long N;
		cin >> N;
		
		if(N == 0)
		{
			cout << "INSOMNIA" << endl;
		}
		else
		{
			long long ret = getLastNumber(N);
			cout << ret << endl;
		}
	}

	return 0;
}
