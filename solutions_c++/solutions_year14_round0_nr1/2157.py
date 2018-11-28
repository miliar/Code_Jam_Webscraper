#include <stdio.h>
int main()
{
	int t1,k;
	scanf("%d",&t1);
	k=t1;
	while(t1--)
	{
		int a,b,x[4],y[4],t[4];
		scanf("%d",&a);
		for(int i=1;i<=4;i++)
		{
			scanf("%d %d %d %d",&t[0],&t[1],&t[2],&t[3]);
			if(a==i)
			{
				x[0]=t[0];x[1]=t[1];x[2]=t[2];x[3]=t[3];
			}
		}
		scanf("%d",&b);
		for(int i=1;i<=4;i++)
		{
			scanf("%d %d %d %d",&t[0],&t[1],&t[2],&t[3]);
			if(b==i)
			{
				y[0]=t[0];y[1]=t[1];y[2]=t[2];y[3]=t[3];
			}
		}
		int count=-1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(x[i]==y[j])
				{
					if(count==-1)count=x[i];
					else count=-2;
					break;
				}
			}
		printf("Case #%d: ",k-t1);
		if(count==-1)
			printf("Volunteer cheated!\n");
		else if(count==-2)
			printf("Bad magician!\n");
		else
			printf("%d\n",count);
	}
	return 0;
}
