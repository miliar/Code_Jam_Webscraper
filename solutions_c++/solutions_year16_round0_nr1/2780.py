#include <iostream>
#include <cstdio>
#include <cstring>

bool b[10];

void mark(int x)
{
	while (x)
	{
		b[x%10]=1;
		x/=10;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		int n,i;
		scanf("%d",&n);
		memset(b,0,sizeof(b));
		for (i=1;i<1000;i++)
		{
			mark(i*n);
			int sum=0,j=0;
			for (;j<10;j++) sum+=b[j];
			if (sum==10) break;
		}
		if (i>=1000) printf("Case #%d: INSOMNIA\n",t);
		else printf("Case #%d: %d\n",t,i*n);
	}
	return 0;
}
