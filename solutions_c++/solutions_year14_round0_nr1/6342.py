#include<Stdio.h>
int main()
{
	int i,j,t,pos,temp,count,k,ans;
	int arr[2][4];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		count=0;
		scanf("%d",&pos);
		for(j=0;j<16;j++)
		{
			if(j>=(pos-1)*4 && j<pos*4)
				scanf("%d",&arr[0][j-(pos-1)*4]);
			else
				scanf("%d",&temp);	
		}
		scanf("%d",&pos);
		for(j=0;j<16;j++)
		{
			if(j>=(pos-1)*4 && j<pos*4)
				scanf("%d",&arr[1][j-(pos-1)*4]);
			else
				scanf("%d",&temp);	
		}
		
		for(k=0;k<4;k++)
		{
			for(j=0;j<4;j++)
			{
				if(arr[0][k]==arr[1][j])
				{
					ans=arr[0][k];
					count++;
				}
				
			}
		}
		if(count>1)
			printf("Case #%d: Bad magician!\n",i);
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",i);
		if(count==1)
			printf("Case #%d: %d\n",i,ans);		
	}
	return 0;
}
