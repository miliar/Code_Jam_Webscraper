#include<stdio.h>
int main()
{
	int test,i,j,l,m,flag,value,s;
	int a[4][4];
	int b[5];
	scanf("%d",&test);
	s=test;
	while(test--)
	{
		flag=0;
		scanf("%d",&l);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
			
		}
		for(j=0;j<4;j++)
		{
			b[j]=a[l-1][j];
		}
		scanf("%d",&m);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
			
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			
				if(b[i]==a[m-1][j])
				{
					flag++;
					value=b[i];
				}
			}
		}
		if(flag==1)
		{
			printf("Case #%d: %d\n",s-test,value);
		}
		if(flag>1)
		{
			printf("Case #%d: Bad magician!\n",s-test);
			
		}
		if(flag==0)
		{
				printf("Case #%d: Volunteer cheated!\n",s-test);
			
		}
		
	}
	return 0;
	
}
