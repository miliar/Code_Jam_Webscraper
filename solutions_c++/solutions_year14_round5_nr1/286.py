#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxN = 2000000;

int T;
long long N, p, q, r, s;
long long a[maxN], sum[maxN];

long long getAns(int i, int j)
{
	long long s[3];
	s[0] = sum[i];
	s[1] = sum[j] - sum[i];
	s[2] = sum[N] - sum[j];
	sort(s, s + 3);
	return s[0] + s[1];
}

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N >> p >> q >> r >> s;
		for (int i = 1; i <= N; i++)
			a[i] = ((i - 1) * p + q) % r + s;
		sum[0] = 0;
		for (int i = 1; i <= N; i++)
			sum[i] = sum[i - 1] + a[i];
		int j = 1;
		long long ans = 0;
		for (int i = 0; i < N; i++)
		{
			while (sum[j] - sum[i] <= sum[N] - sum[j])
				j++;
			ans = max(ans, max(getAns(i, j), getAns(i, j - 1)));
		}
		printf("Case #%d: %.10f\n", z, (double)ans / (double)sum[N]);
	}
	return 0;
}