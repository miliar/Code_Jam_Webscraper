#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

int num_case, len, ans;
char s[200], last;

int main()
{
	//freopen("2.in", "r", stdin);
	//freopen("2.out", "w", stdout);
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%s", s + 1);
		ans = 0;
		len = strlen(s + 1);
		for (int i = 2; i <= len; i++)
			if (s[i] != s[i - 1])
				ans++;
		if (s[len] == '-') ans++;
		printf("Case #%d: %d\n", icase, ans);
	}
	return 0;
}
