#include <iostream>
#include <vector>
using namespace std;
#define ll long long

int main()
{
	int t = 0;
	cin >> t;
	int caseN = 1;
	while (t--)
	{
		ll input;
		cin >> input;
		vector<bool> digits(10);
		int find_count = 0;
		if (input == 0)
			cout << "Case #"<< caseN <<": INSOMNIA\n";
		else
		{
			ll output = input;
			ll i = 1;
			while (find_count != 10)
			{
				output = input * i;
				ll temp = output;
				while (temp)
				{
					if (digits[temp % 10] == false) {
						digits[temp % 10] = true;
						find_count++;
					}
					temp /= 10;
				}
				i++;
			}

			if (find_count == 10)
				cout << "Case #" << caseN << ": " << output << '\n';
		}
		caseN++;
	}
}