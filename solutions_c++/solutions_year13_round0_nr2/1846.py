# include <stdio.h>
# include <iostream>
# include <algorithm>
using namespace std;
int h[110][110],a[110][110],row[110],col[110];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,p,n,m,flag,i,j,max;
	scanf("%d",&t);
	for (p=1;p<=t;++p)
	{
		scanf("%d%d",&n,&m);
		flag = 0;
		for (i=0;i<n;++i)
		{
			max = 0;
			for (j=0;j<m;++j)
			{
				scanf("%d",&h[i][j]);
				a[i][j] = 100;
				if (h[i][j] > max)
					max = h[i][j];
			}
			row[i] = max;	//n;
		}
		for (i=0;i<m;++i)
		{
			max = 0;
			for (j=0;j<n;++j)
				if (h[j][i] > max)
					max = h[j][i];
			col[i] = max; //m;
		}
		for (i=0;i<n;++i)
			for (j=0;j<m;++j)
				a[i][j] = min(a[i][j],row[i]);
		for (i=0;i<m;++i)
			for (j=0;j<n;++j)
				a[j][i] = min(a[j][i],col[i]);
		for (i=0;i<n;++i)
			for (j=0;j<m;++j)
				if (a[i][j]!=h[i][j])
					flag = 1;
		if (flag)
			printf("Case #%d: NO\n",p);
		else
			printf("Case #%d: YES\n",p);
	}
	return 0;
}