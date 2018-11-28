#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string A;

inline void init()
{
	cin >> A;
}

inline int solve()
{
	int i, c = 0;
	char prev = A[0];

	for (i = 1; i < A.length(); i++)
		if (A[i] != prev)
		{
			prev = A[i];
			c++;
		}

	if (prev == '-')
		c++;

	return c;
}

int main()
{
	int T, i;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		init();
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}