#include <cstdio>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

long long ans1(int n, long long p)
{
	long long N = 1LL << n;
	if (p == N)
		return N - 1;
	if (p <= N / 2)
		return 0;
	long long step = N / 2;
	long long step2 = 2;
	long long ret = 0;
	long long pos = 0;
	while(true)
	{
		ret += step2;
		pos += step;
		if (pos + step / 2 >= p)
			return ret;
		step /= 2;
		step2 *= 2;
	}
	return ret;
}

long long ans2(int n, long long p)
{
	long long N = 1LL << n;
	if (p == N)
		return N - 1;
	if (p == 1)
		return 0;
	long long step = N / 2;
	long long step2 = 2;
	long long ret = 0;
	long long pos = 0;
	while(true)
	{
		ret += step;
		pos += step2;
		if (pos >= p - 1)
			return ret;
		step /= 2;
		step2 *= 2;
	}
	return ret;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, t, n, i, j, k;
	long long p;

	cin >> T;
	for(t = 1; t <= T; t++)
	{
		cin >> n >> p;
		
		//cout << ans2(n, p) << " " << ans2s(n, p) << endl;
		printf("Case #%d: ", t);
		cout << ans1(n, p) << " " << ans2(n, p) << endl;
	}

	return 0;
}