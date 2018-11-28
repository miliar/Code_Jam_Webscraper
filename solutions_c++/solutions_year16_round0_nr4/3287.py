#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		int K, C, S;
		cin >> K >> C >> S;

		int S_required = K - (C-1);

		if (S_required > S)
		{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		if (S_required <= 0)
		{
			S_required = 1;
			C = K;
		}

		long long pos = 1;
		for (int c=2; c<=C; c++)
			pos = K * (pos-1) + c;

		cout << "Case #" << t << ":";
		for (int i=0; i<S_required; i++)
			cout << " " << (pos+i);
		cout << endl;
	}
	return 0;
}
