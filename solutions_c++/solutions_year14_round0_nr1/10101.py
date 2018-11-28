#include<stdio.h>
#include<stdlib.h>
int main()
{
	int an,w,s,t,r1,r2,a[4][4],b1[3],b2[3],c=1;
	FILE *f;
	f=fopen("output.txt","w");
	scanf("%d",&t);
	while(t--)
	{w=0;s=0;
		scanf("%d",&r1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==r1-1)
				{
				b1[w]=a[i][j];
				w++;
				}
			}
		}
		w=0;
		scanf("%d",&r2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==r2-1)
				{
				b2[w]=a[i][j];
				w++;
				}
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{if(b1[i]==b2[j])
			{s++;
			an=b1[i];
			if(s>1)
			break;
			}
			}
		}
		system("cls");
		if(s==0)
		fprintf(f,"Case #%d: Volunteer cheated!\n",c);
		else if(s>1)
		fprintf(f,"Case #%d: Bad magician!\n",c);
		else
		fprintf(f,"Case #%d: %d\n",c,an);
		c++;
	}
	fclose(f);
	return 0;
}
