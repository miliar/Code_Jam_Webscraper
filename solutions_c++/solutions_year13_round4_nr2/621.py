#include <iostream>
#include <cstdio>
using namespace std;

string s;
int n, len, m;
int a[101], b[101], c[101];

bool div2()
{
	bool flag = c[0];
	int k = 0;
	for (int i = len; i >= 0; --i) {
		int t = k * 10 + c[i];
		c[i] = (t >> 1);
		k = t&1;
	}
	return flag;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int test, ans1, ans2;
	cin >> test;
	for (int ite = 1; ite <= test; ++ite) {
		cin >> n >> m;
		--m;
		
		int t = 0;
		for (; t < n; ++t)
			if (!(m & (1 << (n - t - 1)))) break;
		if (t == n) ans1 = (1 << n) - 1;
		else ans1 = (1 << (t + 1)) - 2;
		
		for (t = 0; t < n; ++t)
			if (m & (1 << (n - t - 1)))
				break;
		
		for (int i = n - t - 1; i >= 0; --i)
			if (!(m & (1 << i))) {
				++t;
				break;
			}
		ans2 = (1 << n) - (1 << t);
		cout << "Case #" << ite << ": " << ans1 << " " << ans2 << endl;
	}

	return 0;
}
