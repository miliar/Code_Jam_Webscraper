#include<stdio.h>
int main()
{
	freopen("in00.in","r",stdin);
	freopen("out00.txt","w",stdout);
	int t,l=1;
	scanf("%d",&t);
	while(t--)
	{
		int r1,r2,mag[4][4],vol[4][4],i,j;
		scanf("%d",&r1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&mag[i][j]);
		scanf("%d",&r2);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&vol[i][j]);
		int count[17]={0};
		for(i=0;i<4;i++)
		{
			count[mag[r1-1][i]]++;
			count[vol[r2-1][i]]++;
		}
		int count1=0,count2=0;
		for(i=0;i<17;i++)
		{
			if(count[i]==1)
				count1++;
			if(count[i]==2)
				count2++;
		}
		if(count2>=2)
			printf("Case #%d: Bad magician!\n",l++);
		else if(count1==8)
			printf("Case #%d: Volunteer cheated!\n",l++);
		else
		{
			for(i=0;i<17;i++)
			{
				if(count[i]==2){
					printf("Case #%d: %d\n",l++,i);
					break;}
			}
		}
	}
	return 0;
}
