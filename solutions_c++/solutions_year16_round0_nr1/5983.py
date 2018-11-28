#include "stdafx.h"

typedef unsigned long long uint64;

void go(int caseN)
{
	cout << "Case #" << caseN << ": ";

	int N;
	cin >> N;

	if (N != 0)
	{
		int ok[10] = {};

		for (int k = 1; k < 1000; ++k)
		{
			uint64 R = N * k;
//cout << R << endl;
			uint64 M = R;
			for (int j = 0; j < 20; ++j)
			{
				int p = M % 10;
				ok[p] = 1;
				M = M / 10;
				if (M == 0) break;
			}

			int sum = 0;
			for (int i = 0; i < 10; ++i) sum += ok[i];

			if (sum == 10)
			{
				cout << R << endl;
				return;
			}
		}
	}
	cout << "INSOMNIA" << endl;
}



int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");

	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());

	int T; 
	cin >> T;
	for (int t = 1; t <= T; ++t) go(t);
	cin >> T;
    return 0;
}

