#include <stdio.h>

bool digits[10];
bool countdigits(int n)
{
	do
	{
		digits[n % 10] = true;
		n /= 10;
	} while (n);
	for (int i = 0; i < 10; i++)
	{
		if (digits[i] == false) return false;
	}
	return true;
}

int main()
{
	freopen(R"(C:\Users\Unused\Downloads\A-large.in)", "r", stdin);
	freopen(R"(C:\Users\Unused\Downloads\A-large.out)", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		for (int i = 0; i < 10; i++) digits[i] = false;
		printf("Case #%d: ", tt);
		int n;
		scanf("%d", &n);
		if (n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}

		int i;
		for (i = 1; countdigits(n * i) == false; i++);
		printf("%d\n", n * i);
	}
}