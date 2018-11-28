#include <stdio.h>

int a[105][105];
int m,n;

int make(int x,int y)
{
	int f=1;
	for(int i=0;i<n;i++)
		if(a[i][y]>a[x][y])
			f=0;
	if(f)
		return 1;
	f=1;
	for(int i=0;i<m;i++)
		if(a[x][i]>a[x][y])
			f=0;
	if(f)
		return 1;
	return 0;
}

int main(int argc, char const *argv[])
{
	freopen("B-large.in","r",stdin);
	freopen("BBigoutput.txt","w",stdout);
	int t,cass=1;
	scanf("%d",&t);
	while(t--)
	{
		int f=1;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for(int i=0;i<n;i++)
		{
			if(f)
			for(int j=0;j<m;j++)
				if(f)
				{
					if(!make(i,j))
						f=0;
				}
		}
		if(f)
			printf("Case #%d: YES\n",cass++);
		else
			printf("Case #%d: NO\n",cass++);
	}
	return 0;
}
