#include<cstdio>

int main ()
{
	int T, S, ans = 0, cur = 0;
	char c[1003];
	scanf ("%d", &T);
	for (int q = 1; q <= T; q++)
	{
		ans = 0;
		cur = 0;
		scanf ("%d %s", &S, c);
		for (int i = 0; i <= S; i++)
		{
			if (cur < i)
			{
				ans += i-cur;
				cur = i;
			}
			cur+=c[i]-'0';
		}
		printf("Case #%d: %d\n", q, ans);
		
	}
	return 0;

}