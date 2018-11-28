#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,value1[4],value2[4],row,num,res,count;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		count=0;
		scanf("%d",&row);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&num);
				if(i==row-1)
					value1[j]=num;
			}
		}
		scanf("%d",&row);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&num);
				if(i==row-1)
					value2[j]=num;
			}
		}
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(value1[i]==value2[j])
				{
					count++;
					res=value1[i];
				}
			}
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else if(count>1)
			printf("Case #%d: Bad magician!\n",k);
		else
			printf("Case #%d: %d\n",k,res);

	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}