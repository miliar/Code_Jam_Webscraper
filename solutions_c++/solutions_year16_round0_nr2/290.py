#include <bits/stdc++.h>

using namespace std;

char ch[110];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int s = 1; s <= T; s++)
	{
		printf("Case #%d: ", s);
		memset(ch, 0, sizeof ch);
		scanf("%s", ch);
		int ans = 0 - (ch[strlen(ch) - 1] == '+');
		int st = strlen(ch);
		for(int i = 0; i < st; i++) ans += ch[i] != ch[i + 1];
		printf("%d\n", ans);
	}
	return 0;
}
