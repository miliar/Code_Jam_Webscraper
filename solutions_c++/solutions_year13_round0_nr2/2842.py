#include <stdio.h>
#include <string.h>

int d[11000];
int s[11000];
int ans;

int minm(int x, int n, int dx)
{
	int mm=0;
	for(int i=0;i<n;i++)
	{
		if(d[x+i*dx]>mm)mm=d[x+i*dx];
	}
	for(int i=0;i<n;i++)
	{
		if(d[x+i*dx]==mm && !s[x+i*dx])
		{
			s[x+i*dx]=1;
			ans--;
		}
	}
	return mm;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)scanf("%d",&d[i*m+j]);
		}
		memset(s,0,sizeof(s));
		ans=n*m;
		for(int i=0;i<n;i++)minm(i*m,m,1);
		for(int i=0;i<m;i++)minm(i,n,m);
		puts(!ans?"YES":"NO");
	}
	return 0;
}