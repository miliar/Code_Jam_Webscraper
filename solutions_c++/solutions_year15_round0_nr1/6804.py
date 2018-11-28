#include<cstdio>
#include<cstdlib>
int T;
int smax, ans;
char s[1001];
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%d", &smax);
		scanf("%s", s);
		int p = s[0] - '0';
		ans = 0;
		for(int i = 1; i <= smax; i++)
		{
			while(s[i] > '0')
			{
				if(p < i)
				{
					ans += i - p;
					p += i - p;
				}
				p++;
				s[i]--;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}