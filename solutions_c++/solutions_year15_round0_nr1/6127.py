#include<cstdio>

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outputlarge.txt","w",stdout);
	int t=Read();
	char s[1010];
	for(int l=1;l<=t;l++)
	{
		int n=Read();
		if(n==0)
		{
			scanf("%s",s);
			printf("Case #%d: 0\n",l);
			continue;
		}
		int standing=0,ans=0;
		for(int i=0;i<=n;i++)
		{
			int x=getchar()-'0';
			if(x==0)
				continue;
			//printf("%d %d ",i,standing);
			if(standing>=i)
				standing+=x;
			else
				ans+=(i-standing),standing=i+x;
			//printf("%d %d\n",i,standing);
		}
		printf("Case #%d: %d\n",l,ans);
	}
	return 0;
}
