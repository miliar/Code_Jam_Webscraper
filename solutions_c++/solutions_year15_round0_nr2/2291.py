#include <iostream>
using namespace std;

int P[1000];

int main()
{
	int T, count = 0;
	cin >> T;
	while (T--)
	{
		count++;
		int D, result = 1000;
		cin >> D;
		for (int i = 0; i < D; ++i)
			cin >> P[i];

		for (int i = 1; i <= 1000; ++i)
		{
			int sum = i;
			for (int j = 0; j < D; ++j)
			{
				if (P[j] % i == 0)
					sum += P[j] / i - 1;
				else
					sum += P[j] / i;
				if (sum > result)
					break;
			}
			if (sum < result)
				result = sum;
		}
		cout << "Case #" << count << ": " << result << endl;
	}
	return 0;
}