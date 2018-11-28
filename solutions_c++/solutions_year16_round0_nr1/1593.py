#include <iostream>
#include <set>

using namespace std;

int main()
{
	int T;
	unsigned long long N;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		cin >> N;
		bool insomnia = false;
		unsigned long long result = 0;
		if(N == 0) insomnia = true;
		else
		{
			set<int> digits;
			int counter = 1;
			unsigned long long number = N;
			while(digits.size() < 10)
			{
				number = N * counter++;
				while(number != 0)
				{
					int digit = number % 10;
					number /= 10;
					digits.insert(digit);
				}

				if(counter == 100)
				{
					insomnia = true;
					break;
				}
			}
			result = (counter - 1) * N;
		}

		cout << "Case #" << t << ": ";
		if(insomnia) cout << "INSOMNIA" << endl;
		else cout << result << endl;
	}

	return 0;
}