#include <bits/stdc++.h>
using namespace std;
#define maxn 101

char s[maxn];

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t, tn = 1, n, i, ret;
	scanf("%d\n", &t);
	while(t--)
	{
		scanf("%s", s);
		n = strlen(s);
		ret = s[n - 1] == '-';
		for(i = 0; i < n - 1; i++)
			ret += s[i] != s[i + 1];
		printf("Case #%d: %d\n", tn++, ret);
	}
	return 0;
}
