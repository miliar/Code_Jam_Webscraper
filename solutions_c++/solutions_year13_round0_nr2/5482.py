#include <stdio.h>
int ha[105][105],ha1[105][105];

int main()
{
	int i,j,t,n,m,ii,ff;
	freopen("D:\\12.in","r",stdin);
	//freopen("D:\\out.out","w",stdout);
	scanf("%d",&t);
	ii=1;
	while (t--)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&ha[i][j]);
			
			for(i=0;i<n;i++)
			{
				int ma=ha[i][0];
				for(j=1;j<m;j++)
					if(ma<ha[i][j])
						ma=ha[i][j];
					
					
					for(j=0;j<m;j++)
						ha1[i][j]=ma;
			}

			for (i=0;i<m;i++)
			{
				int ma=ha[0][i];
				for(j=1;j<n;j++)
					if(ma!=ha[j][i])
						break;
					if(j==n)
					{
						for(j=0;j<n;j++)
							ha1[j][i]=ma;
					}
			}
			ff=1;
			for (i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
					if(ha[i][j]!=ha1[i][j])
					{ff=0;break;}
					if(!ff)break;
			}
			printf("Case #%d: ",ii++);
			if(!ff)
				printf("NO\n");
			else
				printf("YES\n");
			
	}
	return 0;
}