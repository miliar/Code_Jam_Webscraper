#include <stdio.h>
#include <string.h>

int min_reverse(char s[], int n, char target)
{
	int i;
	i=n-2;
	while (i>=0 && s[i]==s[n-1]) i--;
	if (i<0)
	{
		if (s[n-1]==target) return 0;
		return 1;
	}
	if (s[n-1]==target) return min_reverse(s, i+1, s[n-1]);
	return min_reverse(s, i+1, s[n-1]) + 1;
}

int main()
{
	int t;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		char s[200];
		int len;
		scanf("%s", s);
		len = strlen(s);
		printf("Case #%d: %d\n", cas, min_reverse(s, len, '+'));
	}
	return 0;
}

