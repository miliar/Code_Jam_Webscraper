#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;z++)
	{
		printf("Case #%d: ",z);
		int p,q;
		scanf("%d/%d",&p,&q);
		int gen=0,c=1;
		bool flag = false;
		while (c<q)
		{
			c=c<<1;
			if (c==q)
				flag=true;
		}
		if (flag)
		{
			while(q>p)
			{
				q>>=1;
				gen++;
			}
			printf("%d\n",gen);
		}
		else
			printf("impossible\n");
	}
	return 0;
}