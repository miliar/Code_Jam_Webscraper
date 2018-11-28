#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <cmath>
using namespace std;

bool isPal(int n)
{
	int div = 1;
	while (div * 10 <= n)
		div *= 10;
	while (n)
	{
		if (n % 10 != n / div)
			return false;
		n = (n % div) / 10;
		div /= 100;
	}
	return true;
}

int main(int argc, char *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;

	int A, B;
	for (int t = 1; t <= T; ++t)
	{
		int cnt = 0;
		cin >> A >> B;
		for (int s = A; s <= B; ++s)
		{
			int t = int(sqrt((double)(s+0.1)));
			if (s == t * t && isPal(t) && isPal(s))
				cnt++;
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
