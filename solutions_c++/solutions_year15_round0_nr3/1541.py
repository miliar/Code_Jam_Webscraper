#include <iostream>

using namespace std;

int mul_i(int x)
{
	switch (x)
	{
	case 1: return 2;
	case 2: return -1;
	case 3: return -4;
	case 4: return 3;
	default: return 0;
	}
}

int mul_j(int x)
{
	switch (x)
	{
	case 1: return 3;
	case 2: return 4;
	case 3: return -1;
	case 4: return -2;
	default: return 0;
	}
}

int mul(int x, int y)
{
	int ax = x < 0? -x: x;
	int ay = y < 0? -y: y;
	if (ax == 1 || ay == 1)
		return x * y;
	int res = x;
	if (ay == 2 || ay == 4)
		res = res < 0? -mul_i(-res): mul_i(res);
	if (ay == 3 || ay == 4)
		res = res < 0? -mul_j(-res): mul_j(res);
	return y < 0? -res: res;
}

int main()
{
	int itest, ntest;
	cin >> ntest;
	for (itest = 0; ++itest <= ntest; )
	{
		int n;
		char a[16384];
		long long X;
		cin >> n >> X >> a;
		int x = (int) X % 4;
		if (X < 16)
			x = (int) X;
		else
			x += 16;
		int res = 1, mark = 0;
		for (int i = 0; i < x; ++i)
		for (int j = 0; a[j]; ++j)
		{
			res = mul(res, a[j] - 'i' + 2);
			if (res == 2 && mark == 0)
				mark = 1;
			if (res == 4 && mark == 1)
				mark = 2;
		}
		cout << "Case #" << itest << ": " << (mark == 2 && res == -1? "YES": "NO") << endl;
	}
	return 0;
}
