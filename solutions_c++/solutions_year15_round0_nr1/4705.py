#include <cstdio>
#include <cstring>


void work()
{
	int T,N;
	char a[1024];
	
	scanf("%d",&T);
	
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d",&N);
		scanf("%s", a);
		int ret = 0;
		int tot = 0;
		for (int i=0;i<=N;i++)
		{
			int x = a[i] - '0';
			if (tot < i) {
				ret += i-tot;
				tot = i;
			}
			tot += x;
		}
		printf("Case #%d: %d\n",cas,ret);
	
	}
}

int main()
{
	//int i;
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	work();

	
	return 0;
}
