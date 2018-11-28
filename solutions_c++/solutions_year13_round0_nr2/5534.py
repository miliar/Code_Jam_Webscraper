#include <stdio.h>

int main()
{
	int T,M,N,i,j,k,l,law[100][100],max;
	bool dot[100][100],yes;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		yes=true;
		scanf("%d %d",&N,&M);
		for(j=0;j<N;j++)
			for(k=0;k<M;k++)
			{
				scanf("%d",&law[j][k]);
				dot[j][k]=false;
			}
			
		for(j=0;j<N;j++) // ª½ 
		{
			max=0;
			for(k=0;k<M;k++)
				if(law[j][k]>max)
					max=law[j][k];
			for(k=0;k<M;k++)
				if(law[j][k]==max)
					dot[j][k]=true;
		}
		
		for(j=0;j<M;j++) // ¾î 
		{
			max=0;
			for(k=0;k<N;k++)
				if(law[k][j]>max)
					max=law[k][j];
			for(k=0;k<N;k++)
				if(law[k][j]==max)
					dot[k][j]=true;
		}
		
		for(j=0;j<N;j++)
			for(k=0;k<M;k++)
				if(dot[j][k]==false)
					yes=false;
					
		if(yes)
			printf("Case #%d: YES",i);
		else
			printf("Case #%d: NO",i);
		puts("");
	}
	return 0;
}
