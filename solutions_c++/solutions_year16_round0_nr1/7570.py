#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstring>
#define INF 987654321

using namespace std;

int state;
int t, n;
int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
#endif
	freopen("output4.txt", "w+", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &n);
		state = 0;
		int j = 1;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		for (;;)
		{
			int num = j*n;
			int temp = num;
			while (num)
			{
				state |= 1<<(num % 10);
				num /= 10;
			}
			if (state == 1023) {
				printf("Case #%d: %d\n", i + 1, temp);
				break;
			}
			j++;
		}
	}
}
