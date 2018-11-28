#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		string N;
		cin >> N;

		string num = N;
		int mul = 1;
		bool digits[10] = { false };
		while (true)
		{
			for (int j = 0; j < num.length(); ++j)
				digits[num[j] - '0'] = true;

			bool allSeen = true;
			for (int j = 0; j < 10; ++j)
				if (!digits[j])
				{
					allSeen = false;
					break;
				}

			if (allSeen) break;
			
			// multiplication
			++mul;
			string NN;
			int carry = 0;
			for (int j = N.length() - 1; j >= 0; --j)
			{
				int v = (N[j] - '0') * mul + carry;

				carry = v / 10;
				char c = v % 10 + '0';
				NN = c + NN;
			}

			if (carry != 0) NN = static_cast<char>(carry + '0') + NN;

			num = NN;
			if (num == N) break;
		}

		cout << "Case #" << i << ": ";
		if (num == N)
			cout << "INSOMNIA";
		else
			cout << num;
		cout << endl;
	}
}