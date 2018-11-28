#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

char digs[10];

bool check()
{
	bool res = true;
	for (int i = 0; i < 10 && res; i++)
		res = (res && digs[i]);
	return res;
}

void setNew(int n)
{
	while (n)
	{
		digs[n % 10] = true;
		n /= 10;
	}
}

int solve(int n)
{
	memset(digs, 0, 10);
	int res = 0;
	do
	{
		res += n;
		setNew(res);
	} while (!check());
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		int N;
		scanf("%d", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, solve(N));
	}
	return 0;
}