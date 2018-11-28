#include <cstdio>
#include <cstring>

int main()
{
	int tn;
	scanf("%d",&tn);
	for(int ti = 1; ti <= tn; ++ti)
	{
		char p[128];
		scanf("%s", p);
		int n = strlen(p);
		int ans = 0;
		for(int i = 0; i < n - 1; ++i)
		{
			if(p[i] != p[i+1])
			{
				for(int j = 0; j <= i; j++)
					p[j] = p[j] == '-' ? '+' : '-';
				ans++;
			}
		}
		if(p[n-1] == '-') ans++;
		printf("Case #%d: %d\n", ti, ans);
	}
}
