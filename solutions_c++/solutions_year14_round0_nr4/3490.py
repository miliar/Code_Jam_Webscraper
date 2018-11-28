#include<iostream>
#include<algorithm>
using namespace std;
void main()
{
	int T, N, j, ni, ki, war, dwar, M;
	float n[1000], k[1000];
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		war = dwar = 0;
		cin >> N;
		M = N;
		for (j = 0; j < N; j++)
			cin >> n[j];
		for (j = 0; j < N; j++)
			cin >> k[j];
		sort(n, n + N);
		sort(k, k + N);
		ki = 0;
		for (ni = 0; ni < N; ni++)
		if (n[ni] > k[ki])
		{
			dwar++;
			ki++;
		}
		N = M;
		for (ni = 0; ni < N;ni++)
		for (ki = 0; ki < N;ki++)
		if (k[ki]>n[ni])
		{
			k[ki] = -1;
			war++;
			break;
		}
		war = N - war;
		cout << "Case #" << i << ": " << dwar << " " << war << endl;
	}
}