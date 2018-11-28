#include <stdio.h>
 
int main(void) {
	// your code goes here
	int t,count,value,arr1[4][4],arr2[4][4],arrn1[4],arrn2[4],i,j,ans1,ans2,count1=0;
	scanf("%d",&t);
	while(t--)
	{
		count1++;
		count=0;
		scanf("%d",&ans1);
		for(i=0;i<=3;i++)
			for(j=0;j<4;j++)
				scanf("%d",&arr1[i][j]);
		for(i=0;i<4;i++)
		{
			arrn1[i]=arr1[ans1-1][i];
		}
	scanf("%d",&ans2);
		for(i=0;i<=3;i++)
			for(j=0;j<4;j++)
				scanf("%d",&arr2[i][j]);
		for(i=0;i<4;i++)
		{
			arrn2[i]=arr2[ans2-1][i];
		}
 
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			if(arrn2[i]==arrn1[j])
			{
				count++;
				value=arrn2[i];
			}
		}
 
		if(count==0)
		 printf("Case #%d: Volunteer cheated!\n",count1);
		else if(count>1)
		 printf("Case #%d: Bad Magician!\n",count1);
		else
		 printf("Case #%d: %d\n",count1,value);
 
	}
	return 0;
}
