#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i,t,stand,j,smax,extra;
	char p[1000];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&smax);
		scanf("%s",p);
		stand=(int)(p[0]-48); 
		extra=0;
	 
		for(j=1;j<=smax;j++)
		{
			if(p[j]-48>0)
			{
			if(j<=stand)
			{
				stand=stand+(p[j]-48);
				
			}
			else
			{
				extra=extra+(j-stand);
			 	stand=stand+(p[j]-48)+j-stand;
			}
			}
		  
			 
		}
		printf("Case#%d:%d\n",i+1,extra);
	}
}
