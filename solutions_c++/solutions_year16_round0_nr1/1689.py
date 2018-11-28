#include <bits/stdc++.h>
using namespace std;

int mark[30];

void solve(int x)
{
	int tmp;
	int ch;
	if (x==0)
	{
		printf("INSOMNIA\n");
		return ;
	}
	for (int i=1;i<=99999;i++)
	{
		tmp = i*x;
		while (tmp)
		{
			mark[tmp%10] = 1;
			tmp/=10;
		}
		ch = 1;
		for (int j=0;j<=9;j++)
			if (!mark[j]) ch = 0;
		if (ch)
		{
			printf("%d\n",i*x);
			return ;
		}
	}
	return ;
}


int main()
{
	int q,n;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&q);
	for (int x=1;x<=q;x++)
	{
		for (int j=0;j<=9;j++)
			mark[j] = 0;
		printf("Case #%d: ",x);
		scanf("%d",&n);
		solve(n);
	}
	return 0;
}