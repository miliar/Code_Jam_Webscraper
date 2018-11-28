#include <stdio.h>
#include <iostream>

using namespace std;

#define INSOMNIA "INSOMNIA"


long long solve(int x) {
	if (x == 0) {
		return -1;
	}

	int t = x;
	int mask = 0;

	while (true)
	{
		int s = t;
		while (s) {
			mask |= (1 << (s % 10));
			s /= 10;
		}

		if (mask == 1023) {
			return t;
		}

		t += x;
	}
}

const int MAXN = 1000005;
long long result[MAXN];

void precalc()
{
	for (int i = 0; i < MAXN; i++)
	{
		result[i] = solve(i);
	}
}

int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	precalc();

	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int x;
		cin >> x;

		long long res = result[x];

		cout << "Case #" << (i + 1) << ": ";
		if (res < 0)
		{
			cout << INSOMNIA;
		}
		else {
			cout << res;
		}
		cout << endl;
	}

	return 0;
}