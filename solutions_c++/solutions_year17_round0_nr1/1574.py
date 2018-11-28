#include<cstdio>


char s[1005];

int T,k;

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%s",s + 1);
		int len = 1;
		while (s[len]) len ++;
		len --;
		scanf("%d",&k);
		int cnt = 0;
		for (int i = 1; i <= len - k + 1; i ++)
			if (s[i] == '-')
			{
				cnt ++;
				for (int j = 0; j <= k - 1; j ++)
					if (s[i + j] == '+')
						s[i + j] = '-';
					else 
						s[i + j] = '+';
			}
		bool flag = 1;
		for (int i = 1; i <= len; i ++)
			if (s[i] == '-')
				flag = 0;
		if (flag)
			printf("Case #%d: %d\n",t,cnt);
		else 
			printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}
