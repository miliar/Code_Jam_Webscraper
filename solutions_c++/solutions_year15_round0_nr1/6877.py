#include <iostream>

using namespace std;

int main()
{
	int T, N;
	int smax;
	
	cin >> T;

	for (int k = 1; k <= T; k++)
	{

		char str[2000];
		int sum = 0;
		int rem = 0;

		cin >> N;

		cin >> str;

		sum = str[0] - '0';
		for (int i = 1; i <= N; i++)
		{
			int no = str[i] - '0';
			if (i > sum && no != 0)
			{
				rem += i - sum;
				sum = sum + no + (i - sum);
			}
			else
				sum += no;
		}

		cout << "Case #" << k << ": " << rem << endl;
		rem = 0;
		sum = 0;
	}
	return 0;
}
