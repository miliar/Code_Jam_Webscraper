#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>

using namespace std;

int getBin(int x)
{
	int ans = 0;
	while (x > 0)
	{
		ans |= (1 << x % 10);
		x /= 10;
	}
	return ans;
}

int getLast(int x)
{
	int final = 0, ans, need = 1023;
	for (int i = 1; final != need; ++i)
	{
		ans = i * x;
		final |= getBin(ans);
	}
	return ans;
}

void caseN(int number, int x)
{
	printf("Case #%d: ", number);
	if (x == 0)
		printf("INSOMNIA");
	else
		printf("%d", getLast(x));
	printf("\n");
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		int x;
		scanf("%d", &x);
		caseN(i + 1, x);
	}

	return 0;
}