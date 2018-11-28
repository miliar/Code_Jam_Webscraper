#include <stdio.h>

int main()
{
	int t;
	int a;
	int card,vis[20];
	int count,w;
	
	scanf("%d",&t);
	
	for(int i1=1;i1<=t;i1++)
	{
		for(int i2=0;i2<=16;i2++)
		{
			vis[i2]=1;
		}
		scanf("%d",&a);
		for(int i2=0;i2<4;i2++)
		{
			for(int i3=0;i3<4;i3++)
			{
				scanf("%d",&card);
				if(i2+1!=a)
				{
					vis[card]=0;
				}
			}
		}
		scanf("%d",&a);
		for(int i2=0;i2<4;i2++)
		{
			for(int i3=0;i3<4;i3++)
			{
				scanf("%d",&card);
				if(i2+1!=a)
				{
					vis[card]=0;
				}
			}
		}
		count=0;
		for(int i2=1;i2<=16;i2++)
		{
			if(vis[i2]==1)
			{
				count++;
				w=i2;
			}
		}
		if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",i1); 
		}else if(count==1){
			printf("Case #%d: %d\n",i1,w);
		}else{
			printf("Case #%d: Bad magician!\n",i1);
		}
	}
	
	return 0;
}

