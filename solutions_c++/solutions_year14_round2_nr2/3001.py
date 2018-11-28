#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(0);
	int T;

	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		int A,B;

		int K;

		cin >> A;
		cin >> B;
		cin >> K;

		int res = 0;

		for (int i = 0; i < A; ++i)
		{
			for (int j = 0; j < B; ++j)
			{
				if ((i&j) < K)
					res ++;
			}
		}

		cout << "Case #" << t + 1 <<": "<< res << '\n';
	}

	return 0;
}