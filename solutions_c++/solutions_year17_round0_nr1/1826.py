#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(std::string &S, int K)
{
	int flips = 0;
	for (int i = 0; i < S.size(); ++i)
		if (S[i] != '+')
		{
			if (i + K > S.size())
				return -1;
			for (int j = 0; j < K; ++j)
				S[i+j] = S[i+j] == '+' ? '-' : '+';
			++flips;
		}
	return flips;
}

int main()
{
	std::ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int K;
		string S;
		cin >> S >> K;
		int res = solve(S, K);
		cout << "Case #" << i + 1 << ": ";
		if (res < 0)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << std::endl;
	}
	return 0;
}
