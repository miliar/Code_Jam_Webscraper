#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	getchar();
	for (int tt = 1; tt <= t; tt++)
	{
		char a[200];
		gets(a);
		int len = strlen(a);
		int i = 0;
		int flag = 0;
		int cnt = 0;
		while (i < len && a[i] == '-')
		{
			flag = 1;
			i++;
		}
		if (flag) cnt++;

		for (; i < len; i++)
		{
			int flag = 0;
			if (a[i] == '-')
			{
				while (i < len && a[i] == '-')
				{
					flag = 1;
					i++;
				}
			}
			if (flag) cnt += 2;
		}
		printf("Case #%d: %d\n", tt, cnt);
	}
	return 0;
}
