#include<stdio.h>
char s[201];
int solve()
{
	scanf("%s", s);
	int c=1, i;
	for(i=1; s[i]; i++)
	{
		if(s[i]!=s[i-1]) c++;
	}
	if(s[i-1] == '+') c--;
	return c;
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int TT=1; TT<=T; TT++)
	{
		printf("Case #%d: %d\n", TT, solve());
	}
	return 0;
}
