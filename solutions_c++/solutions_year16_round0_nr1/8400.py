#include <array>
#include <iostream>

using namespace std;

void main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;

		if (N == 0)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		}
		else
		{
			array<bool, 10> digits;
			digits.fill(false);

			for (int j = 1; ; ++j)
			{
				auto Ni = j * N;
				while (Ni > 0)
				{
					digits[Ni % 10] = true;
					Ni /= 10;
				}

				if (std::find(digits.begin(), digits.end(), false) == digits.end())
				{
					cout << "Case #" << i + 1 << ": " << j * N << endl;
					break;
				}
			}
		}
	}
}
