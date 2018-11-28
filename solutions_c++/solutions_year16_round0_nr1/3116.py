#include <iostream>

using namespace std;

int changeDigit(int n, int digit[10]) {
	int count = 0, curdigit;
	int tempn = n;
	while(tempn != 0) {
		curdigit = tempn % 10;
		if (digit[curdigit] == 0)
		{
				digit[curdigit] = 1;
				count++;
		}
		tempn /= 10;
	}

	return count;
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
			int N, times = 1, count = 0, curcount;
			int digit[10];
			long long result;
			for (int j = 0; j < 10; ++j)
			{
				digit[j] = 0;
			}
			cin >> N;

			if (N == 0)
			{
				cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
				continue;
			}

			while(true) {
				curcount = changeDigit(times * N, digit);
				count += curcount;
				if (count >= 10)
				{
					result = times * N;
					break;
				}
				times++;
			}

			cout << "Case #" << i + 1 << ": " << result << endl;

	}

	return 0;
}