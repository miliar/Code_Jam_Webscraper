#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		int S;
		cin >> S;

		string shyness;
		cin >> shyness;

		int ret = 0;
		int total = 0;
		for (int j = 0; j <= S; ++j)
		{
			int n = shyness[j] - '0';
			if (n != 0)
			{
				if (total < j)
				{
					ret += j - total;
					total = j + n;
				}
				else
				{
					total += n;
				}
			}
		}

		cout << "Case #" << i << ": " << ret << endl;
	}

	return 0;
}