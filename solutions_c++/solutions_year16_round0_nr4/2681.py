#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T, K, C, S;
	unsigned long long i, N, M;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> K >> C >> S;

		N = pow(K, C);
		M = (double) N / S;

		cout << "Case #" << t << ":";
		for (i = 0; i < S; i++)
			cout << " " << i*M + 1;
		cout << endl;
	}
	
	return 0;
}

#endif