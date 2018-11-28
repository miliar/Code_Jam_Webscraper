#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;


int T;

void print(int idx, int n)
{
	if (n != -1)
		printf("Case #%d: %d\n", idx, n);
	else printf("Case #%d: INSOMNIA\n", idx);
}

int main()
{
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		set<int> digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		int n;
		scanf("%d", &n);
		if (n == 0)
		{
			print(cases, -1);
			continue;
		}
		int sum = 0;
		while (!digits.empty())
		{
			sum += n;
			int x = sum;
			while (x)
			{
				if (digits.find(x % 10) != digits.end())
					digits.erase(x % 10);
				x /= 10;
			}
		}
		print(cases, sum);
	}
	return 0;
}