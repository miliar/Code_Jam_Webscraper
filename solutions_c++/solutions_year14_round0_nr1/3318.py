#include <iostream>
#include <cstdio>
#include <cstdlib>


int main()
{
	FILE  *f1,*f2;
	f1=fopen("A-small-attempt0.in","r");
	f2=fopen("output.txt","w");
	int t,i,j,temp=0,c;
	int a[5][5],b[5][5];
	int x,y;
	fscanf(f1,"%d",&t);
	for(int k=0;k<t;k++)
	{
		fscanf(f1,"%d",&x);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fscanf(f1,"%d ",&a[i][j]);
			}
		}
		fscanf(f1,"%d",&y);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fscanf(f1,"%d ",&b[i][j]);
			}
		}
		c=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//printf("%d %d %d\n",a[x-1][i],b[y-1][j],x);
				if(a[x-1][i]==b[y-1][j])
					{c++;temp=a[x-1][i];}
			}
		}
		
		if(c==0)
			fprintf(f2,"Case #%d: Volunteer cheated!\n",k+1);
		else if(c==1)
			fprintf(f2,"Case #%d: %d\n",k+1,temp);
		else if(c>1)
			fprintf(f2,"Case #%d: Bad magician!\n",k+1);


		




	}
fclose(f1);
		fclose(f2);
}