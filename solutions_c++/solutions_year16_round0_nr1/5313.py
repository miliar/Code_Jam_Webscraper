#include <cstdlib>
#include <cstdio>
#include <cstring>

int solve(int n)
{
	if (n == 0) return -1;
	int ans = 0;
	int tmp[20];
	memset(tmp,0,sizeof(tmp));
	while (tmp[11]<10)
	{
		++ans;
		int k = n * ans;
		while (k)
		{
			int i = k % 10;
			k = k / 10;
			if (tmp[i]==0)
			{
				tmp[i]=1;
				tmp[11]++;
			}
		}
	}
	return ans*n;
}

int main()
{
	int T,n;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		scanf("%d",&n);
		printf("Case #%d: ",i);
		int ans = solve(n);
		if (ans == -1)
			printf("INSOMNIA");
		else
			printf("%d",ans);
		printf("\n");
	}
	
	return 0;
	
}