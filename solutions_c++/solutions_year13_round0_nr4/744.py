#include <stdio.h>
#include <string.h>

int tx[1<<20];
int fx[1<<20];

int main()
{
	long long tc,t;
	int k,n,i,j;
	int a[201];
	int r[201];
	int m[201];
	int c[201][400];
	scanf("%lld\n",&t);
	for (tc=0;tc<t;++tc)
	{
		scanf("%d %d",&k,&n);
		memset(a,0,201*sizeof(a[0]));
		for (i=0;i<k;++i)
		{
			scanf("%d",&j);
			++a[j];
		}
		for (i=0;i<n;++i)
		{
			scanf("%d %d",r+i,m+i);
			for (j=0;j<m[i];++j) scanf("%d",c[i]+j);
		}
		fx[0]=1;
		for (i=1;i<(1<<n);++i) fx[i]=0;
		for (i=0;i<(1<<n);++i)
		{
			if (fx[i]==0)
			{
				tx[i]=0;
				continue;
			}
			tx[i]=1;
			for (j=0;j<n;++j) if (i&(1<<j))
			{
				for (k=0;k<m[j];++k)
				{
					++a[c[j][k]];
				}
			}
			for (j=0;j<n;++j) if (i&(1<<j))
			{
				--a[r[j]];
				if (a[r[j]]<0) tx[i]=0;
			}
			if (tx[i])
			{
				for (j=0;j<n;++j) if ((i&(1<<j))==0)
				{
					if (a[r[j]]>0) fx[i+(1<<j)]+=(1<<j);
				}
			}
			for (j=0;j<n;++j) if (i&(1<<j))
			{
				++a[r[j]];
			}
			for (j=0;j<n;++j) if (i&(1<<j))
			{
				for (k=0;k<m[j];++k)
				{
					--a[c[j][k]];
				}
			}
		}
		for (i=(1<<n)-2;i>=0;--i)
		{
			k=0;
			for (j=0;j<n;++j)
				if ((i&(1<<j))==0) 
					if ((fx[i+(1<<j)]&(1<<j))!=0) ++k;
			if (k==0) fx[i]=0;
		}
		printf("Case #%lld: ",tc+1);
		if (fx[(1<<n)-1]==0)
		{
			printf("IMPOSSIBLE\n");
		} else
		{
			i=0;
			j=0;
			while (i<(1<<n)-1)
			{
				k=0;
				while ((i&(1<<k))!=0 || ((fx[i+(1<<k)])&(1<<k))==0) ++k;
				printf("%d ",1+k);
				i+=(1<<k);
			}
			printf("\n");
		}
	}
	return 0;
}
