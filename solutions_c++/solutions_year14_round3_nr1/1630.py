#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int p,q,ans;
	int t,T;
	scanf("%d",&t);
	for (T = 1;T <= t;T++)
	{
		scanf("%d/%d",&p,&q);
		ans = 0;
		while (q > 1)
		{
			if (q % 2 != 0)
			{
				ans = -1;
				break;
			}
			else
			{
				q /= 2;
				ans++;
			}
		}
		printf("Case #%d: ",T);
		if (ans == -1) printf("impossible\n");
		else
		{
			while (p > 1)
			{
				if (p % 2 == 1) p--;
				p /= 2;
				ans--;
			}
			printf("%d\n",ans);
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
