#include <iostream>

using namespace std;

void solve(int t)
{
	int n;
	cin >> n;

	if (!n)
	{
		cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
		return;
	}

	bool digits[10];
	int ndigits = 0;
	for (int i = 0; i < 10; ++i)
		digits[i] = 0;

	for (int i = 1; ; ++i)
	{
		int curr = n * i;
		//cout << curr << endl;
		while (curr)
		{
			int digit = curr % 10;
			//cout << "digit " << digit << endl;
			if (!digits[digit])
			{
				digits[digit] = true;
				++ndigits;
				if (ndigits == 10)
				{
					cout << "Case #" << t + 1 << ": " << n * i << endl;
					return;
				}
			}
			curr /= 10;
		}
	}
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		solve(i);
	}
	return 0;
}
