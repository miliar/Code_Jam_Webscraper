#include<bits/stdc++.h>
using namespace std;

#define MAXLEN 106

char str[MAXLEN];

int main()
{
	freopen("Binhard.txt", "r", stdin);
	freopen("Bouthard.txt", "w", stdout);
	int t,T;
	bool st;
	int cnt,i;
	scanf("%d", &T);
	for (t=1; t<=T; ++t)
	{
		scanf("%s", str);
		cnt = 1;
		st = str[0] == '+' ? 1:0;
		for (i=1; str[i]; ++i)
		{
			if (str[i] == str[i-1]) continue;
			++cnt;
		}
		if (str[i-1] == '+') --cnt;
		printf("Case #%d: %d\n", t,cnt);
	}
	return 0;
}