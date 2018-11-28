
#include<iostream>
#include<string.h>
using namespace std;

int sol(char *s, int l, bool flag)
{
	while (l > 0 && (s[l - 1] == '+') != flag)
		l--;
	return l == 0 ? 0 : 1 + sol(s, l, !flag);
}

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		char s[101];
		scanf("%s", s);
		printf("Case #%d: ", cases);
		printf("%d\n", sol(s, strlen(s), false));
	}
	//system("pause");
	return 0;
}