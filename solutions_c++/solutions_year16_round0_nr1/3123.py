#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		long long n, m = 0, x = 0x3FF;

		cin >> n;
		for (int i = 0; x && i < 1000; i++) {
			m += n;
			for (long long t = m; t; t /= 10) x &= ~(1 << (t % 10));
		}

		if (x == 0)
			printf("Case #%d: %lld\n", ti, m);
		else
			printf("Case #%d: INSOMNIA\n", ti);
	}

	return 0;
}
