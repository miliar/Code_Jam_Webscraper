#include <iostream>

using namespace std;

int main()
{
	int itest, ntest;
	cin >> ntest;
	for (itest = 0; ++itest <= ntest; )
	{
		int n, a[1024];
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		int res = a[0];
		for (int i = 0; i < n; ++i)
			if (res < a[i])
				res = a[i];
		for (int max = 1; max < res; ++max)
		{
			int t = max;
			for (int i = 0; i < n; ++i)
			{
				if (a[i] <= max)
					continue;
				t += (a[i] - 1) / max;
			}
			if (t < res)
				res = t;
		}
		cout << "Case #" << itest << ": " << res << endl;
	}
	return 0;
}
