#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

void answer(long long a, int t)
{
	cout << "Case #" << t + 1 << ": " << a << '\n';
}

int main()
{
	int T, N;
	cin >> T;
	vector<long long> D(10), H(10), M(10);
	for (int t = 0; t < T; ++t)
	{
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> D[i] >> H[i] >> M[i];

		if (N < 2)
			answer(0, t);
		else
		{
			if (M[0] == M[1])
			{
				answer(0, t);
				continue;
			}
			if (M[1] < M[0])
			{
				swap(D[0], D[1]);
				swap(H[0], H[1]);
				swap(M[0], M[1]);
			}
			D[0] -= 360;

			if (360 * (M[1] - M[0]) >= D[0] * (M[1] - M[0]) + M[1] * (D[1] - D[0]))
				answer(1, t);
			else
				answer(0, t);
		}
	}
	return 0;
}