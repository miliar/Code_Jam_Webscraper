#include <cstdio>

int T,p,a,b,f[17];

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
	{
		b=0;
		for (int i=1;i<=16;++i) f[i]=0;
		scanf("%d",&p);
		for (int i=1;i<=4;++i) for (int j=1;j<=4;++j)
		{
			scanf("%d",&a);
			f[a]+=i==p;
		}
		scanf("%d",&p);
		for (int i=1;i<=4;++i) for (int j=1;j<=4;++j)
		{
			scanf("%d",&a);
			f[a]+=i==p;
		}
		for (int i=1;i<=16;++i) if (f[i]==2) a=i,++b;
		printf("Case #%d: ",t);
		if (b==0) puts("Volunteer cheated!");
		else if (b==1) printf("%d\n",a);
		else puts("Bad magician!");
	}
	return 0;
}