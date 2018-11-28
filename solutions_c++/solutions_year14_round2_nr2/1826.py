#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		int A,B,K;
		cin >> A >> B >> K;

		int count = 0;
		for (int i = 0; i < A; ++i)
		{
			for (int j = 0; j < B; ++j)
			{
				if((i&j) < K)
					++count;
			}
		}
		cout << "Case #" << t << ": " << count << "\n";
	}
	return 0;
}