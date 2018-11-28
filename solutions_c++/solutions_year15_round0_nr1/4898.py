#include<stdio.h>
#include<string.h>
int main()
{
	int t;
	scanf("%d", &t);
	for(int q=1;q<=t;q++)
	{
		int l;
		char s[1005];
		scanf("%d%s", &l, s);
		int cur=0, ans=0;
		for(int i=0;i<=l;i++)
		{
			if(cur<i)
			{
				ans+=i-cur;
				cur=i;
			}
			cur+=s[i]-48;
		}
		printf("Case #%d: %d\n", q, ans);
	}
	return 0;
}
