#include <bits/stdc++.h>

using namespace std;

int i, j, t, ans = 0;
char s[110];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.ans", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%s", s);
		ans = 0;
		for (j = 0; j < strlen(s); j++)
			if (s[j] == '-') {
				ans++;
				while (j < strlen(s) && s[j] == '-') j++;
			}
		if (s[0] == '-')
			ans = (ans - 1) * 2 + 1;
		else
			ans = ans * 2;
		
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
	return 0;
}