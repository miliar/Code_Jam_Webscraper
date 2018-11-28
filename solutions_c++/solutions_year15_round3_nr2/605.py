#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <string>
using namespace std;
int k, l, s, i, t, cnt[30], j, mx, x, time;
double ans;
string str1, str2;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("l_out.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		memset(cnt, 0, sizeof(cnt));
		scanf("%d%d%d", &k, &l, &s);
		cin >> str1 >> str2;
		for (j = 0; j < k; j++)
			cnt[str1[j]-'A']++;
		mx = 0;
		for (x = 1; x < l; x++)
		{
			if (str2.substr(0, x) == str2.substr(l - x, x))
			{
				mx = x;
			}
		}
		time = 1;
		time += (s - l) / (l - mx);
		ans = s-l+1;
		for (j = 0; j < l; j++)
		{
			if (cnt[str2[j]-'A'] == 0)
			{
				printf("Case #%d: 0\n", i);
				break;
			}
			ans *= (double)cnt[str2[j]-'A']/(double)k;
		}

		if (j==l)
		{
			printf("Case #%d: %lf\n", i, time - ans);
		}
	}
	return 0;
}