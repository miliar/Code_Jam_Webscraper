#include <stdio.h>
#include <algorithm>
int main()
{
	int a,b[120][120];
	int i,j,k,l,n,m,flagx,flagy,ww;
	scanf("%d",&a);
	for(k=1; k<=a; k++)
	{
		scanf("%d",&n);
		scanf("%d",&m);
		//printf("n,m : %d %d\n",n,m);
		for(i=0; i<n; i++)
			for(j=0; j<m; j++)
				scanf("%d",&b[i][j]);
		ww=1;
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				flagx=1;
				flagy=1;
				for(l=0; l<m; l++)
				{
					if(b[i][j]<b[i][l])
						{flagx=0;break;}
				}
				for(l=0; l<n; l++)
				{
					if(b[i][j]<b[l][j])
						{flagy=0;break;}
				}
				if((flagx==1)||(flagy==1))
					continue;
				else
				{
					ww=0;
					break;
				}
			}
			if(ww==0)
				break;
		}
		if(ww==1)
			printf("Case #%d: YES\n",k);
		else
			printf("Case #%d: NO\n",k);
	}
	return 0;
}