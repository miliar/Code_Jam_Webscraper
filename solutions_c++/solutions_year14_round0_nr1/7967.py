#include<stdio.h>
int main()
{
	int t,ans1,k=0,i,z,j,a[4][4],arr[4],n,ans2,sum=0,d=1;
	scanf("%d",&t);
	for(;t--;)
	{
		k=sum=0;
	scanf("%d",&ans1);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			scanf(" %d",&a[i][j]);
			if(ans1==(i+1))
			arr[k++]=a[i][j];
		}
		//printf("\n");
	}
scanf("%d",&ans2);
for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
	{
		scanf(" %d",&a[i][j]);
	}
	//printf("\n");
}

for(i=0;i<4;i++)
{

	for(j=0;j<4;j++)
	{
	if(arr[i]==a[ans2-1][j])
	{
	sum++;z=a[ans2-1][j];
	}
	}
}
if(sum==0)
printf("case #:%d Volunteer cheated!\n",d++);
else if(sum==1)
printf("case #:%d %d\n",d++,z);
else
printf("case #:%d bad magician!\n",d++);
}
}
