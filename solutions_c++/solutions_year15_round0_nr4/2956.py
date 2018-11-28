#include<stdio.h>

int main()
{
	FILE *fp,*fp1;
	
	fp=freopen("D-small-attempt0.in","r",stdin);
	fp1=freopen("x.text","w+",stdout);
	
	int t,i,x,r,c;
	
	scanf("%d",&t);
	
	for(i=0;i<t;i++)
	{
		scanf("%d%d%d",&x,&r,&c);
		
		if((r*c)%x!=0)
			printf("Case #%d: RICHARD\n",i+1);
		else
		{
			if(x==1)
				printf("Case #%d: GABRIEL\n",i+1);
			else if(x==2)
				printf("Case #%d: GABRIEL\n",i+1);
			else if(x==3)
			{
				if(r*c==3)
					printf("Case #%d: RICHARD\n",i+1);
				else
					printf("Case #%d: GABRIEL\n",i+1);
			}
			else
			{
				if(r*c>=12)
					printf("Case #%d: GABRIEL\n",i+1);
				else
					printf("Case #%d: RICHARD\n",i+1);
			}
			
		}
	}
	fclose(fp);
	fclose(fp1);
	
	return 0;
}
