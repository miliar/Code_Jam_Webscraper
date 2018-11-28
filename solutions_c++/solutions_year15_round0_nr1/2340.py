#include <iostream>
using namespace std;

int main()
{
	int T, count = 0;
	cin >> T;
	while (T--){
		count++;
		int Smax, sum = 0;
		int result = 0;
		char c;

		cin >> Smax;
		for (int i = 0; i <= Smax; ++i)
		{
			if (sum < i)
			{
				result += i - sum;
				sum = i;
			}
			cin >> c;
			sum += c - '0';
		}
		cout << "Case #" << count << ": " << result << endl;
	}
	return 0;
}

