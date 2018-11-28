#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;

	cin >> T;

	for (int case_i = 0; case_i < T; ++case_i)
	{

		int smax;

		cin >> smax;

		string digits;

		cin >> digits;

		int n_required = 0;
		int currently_clapping = 0;
		for (int i = 0; i <= smax; ++i)
		{
			if (currently_clapping < i)
			{
				n_required += i - currently_clapping;
				currently_clapping = i;
			}
			currently_clapping += digits.at(i)- '0';
		}

		cout << "Case #" << case_i+1 << ": " << n_required << endl;

	}
	return 0;
}