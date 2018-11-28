#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

int count(int i)
{
	int res = 0;
	while(i)
	{
		res += i & 1;
		i >>= 1;
	}
	return res;
}

int equal_bit(int m, int l, int r)
{
	//cout << m << ' ' << l << ' ' << r << endl;

	return ((m & (1 << l)) > 0) & ((m & (1 << r)) > 0);
}

int noise(int mask, int R, int C)
{
	//cout << mask << ' ' << R << ' ' << C << endl;
	int res = 0;
	for (int i = 0; i < R*C; ++i)
	{
		if (i + R < R*C)
		{
			res += equal_bit(mask, i, i + R);
		}
		if (i - R >= 0)
		{
			res += equal_bit(mask, i, i - R);
		}
		if (i % R != 0)
		{
			res += equal_bit(mask, i, i - 1);
		}
		if (i % R != R - 1)
		{
			res += equal_bit(mask, i, i + 1);
		}
	}
	//cout << "RESSS" <<  res << endl;
	return res;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int R, N, C;
		int answer = 10000000;
		cin >> R >> C >> N;
		for (int i = 0; i < (1 << (R * C)); ++i)
		{
			if (count(i) == N)
			{
				answer = min(answer, noise(i, R, C));
			}
		}
		cout << "Case #" << t + 1 << ": " << answer / 2 << '\n';
	}


	return 0;
}