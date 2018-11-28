#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn)
	{
		long long n, p;
		cin >> n >> p;
		long long r1, r2;
		p--;
		for (int i = 0; i <= n; ++i) 
		{
			if (p + 1 >= (1ll << (n - i))) {
				r2 = (1ll << n) - (1ll << i);
				break;
			}
		}
		p++;

		for (int i = 0; i <= n; ++i) 
		{
			if (p <= (1ll << n) - (1ll << i)) {
				r1 = (1ll << (n - i)) - 2;
			}
		}

		if (p == 1) r1 = 0;
		if (p == (1ll << n)) r1 = p - 1;
		cout << "Case #" << cn << ": " << r1 << " " << r2 << endl;
	}
}
