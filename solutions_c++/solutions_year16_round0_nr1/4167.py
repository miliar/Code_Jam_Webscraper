#include <iostream>
#include <cstring>
#include <string>

using namespace std;

#define LL long long

LL n, t;
bool hashTab[10];

LL solve()
{
	if (n == 0)
		return -1;

	memset(hashTab, false, sizeof(bool) * 10);
	LL cnt = 0, k = 1, x = n;

	while (true)
	{
		x = k * n;
		while (x > 0)
		{
			if (!hashTab[x % 10])
			{
				hashTab[x % 10] = true;
				cnt++;
				if (cnt == 10)
					break;
			}

			x /= 10;
		}

		if (cnt == 10)
			break;

		k++;
	}

	return k * n;
}

void getInput()
{
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> n;

		LL status = solve();
		if (status == -1)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %lld\n", i, status);
	}
}

int main(int argc, char const *argv[])
{
	getInput();
	return 0;
}