#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n, t;
    cin >> t;
    for (int i = 1; i <= t; i++)
	{
		cin >> n;
		cout << "Case #" << i << ": ";
		if (n == 0) cout << "INSOMNIA";
		else
		{
			unsigned long long mul = 1;
			unsigned long long cn;
			map<int, int> digits;
			do
			{
				cn = n * mul;
				mul++;
				unsigned long long rem = cn;
				do
				{
					int digit = rem % 10;
					rem /= 10;
					digits[digit] = 1;
				} while (rem);
			} while (digits.size() != 10);
			cout << cn;
		}
		cout << endl;
	}
}
