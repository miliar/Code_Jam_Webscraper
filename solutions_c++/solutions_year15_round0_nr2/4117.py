#include <iostream>
#include <algorithm>

using namespace std;

int _t;
int n;
int a[1005];
int b[1005];
int ans;


void check()
{
	int q = 0;
	int mt = 0;
	for (int i = 0; i < n; ++i)
	{
		int t = a[i] / b[i];
		if (a[i] % b[i]) ++t;
		q += b[i] - 1;
		mt = max(mt, t);
	}
	ans = min(ans, q + mt);
}

void rec(int k)
{
	if (k == n)
		check();

	for (int i = 1; i <= a[k]; ++i)
	{
		b[k] = i;
		rec(k + 1);
		b[k] = 0;
	}
}

int main()
{
	cin >> _t;
	for (int _i = 0; _i < _t; ++_i)
	{
		cin >> n;
		for (int i = 0; i < 1005; ++i)
		{
			a[i] = 0;
			b[i] = 0;
		}

		for (int i = 0; i < n; ++i)
			cin >> a[i];
		ans = 1000;
		rec(0);
		
		cout << "Case #" << _i + 1 << ": " << ans << endl;
	}
	return 0;
}