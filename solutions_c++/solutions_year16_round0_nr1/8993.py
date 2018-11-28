#include <iostream>
#include <algorithm>

using namespace std;

bool has(bool digit[10])
{
	for (int i = 0; i < 10; i++)
	{
		if (!digit[i]) return false;
	}

	return true;
}

int main()
{
	bool ok = true;

	long long t, n, last = 0, counter = 1, cur = 0;

	cin >> t;

	while (t--)
	{
		cin >> n;

		bool digit[10] = { false };

		long long temp = 0;

		ok = true;

		temp = n;

		for (int i = 1; i < 100000 && ok; i++)
		{
			n *= i;

			cur = n;

			while (n > 0)
			{
				digit[n % 10] = true;

				n /= 10;
			}

			if (has(digit))
			{
				cout << "Case #" << counter << ": " << cur << endl;

				ok = false;

				break;
			}

			n = temp;
		}

		if (ok)
		{
			cout << "Case #" << counter << ": " << "INSOMNIA" << endl;
		}

		counter++;
	}
}



