#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	FILE *p=NULL;
	p=fopen("input1.txt","r");
	int t,x;
	fscanf(p,"%d",&t);
	int a1[4][4],b[t],c1[4],a2[4][4],c2[4],f;
	for(int i=0;i<t;i++)
	{
		fscanf(p,"%d",&x);f=0;
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		fscanf(p,"%d",&a1[j][k]);
		for(int j=0;j<4;j++)
		c1[j]=a1[x-1][j];
		fscanf(p,"%d",&x);
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		fscanf(p,"%d",&a2[j][k]);
		for(int j=0;j<4;j++)
		c2[j]=a2[x-1][j];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			if(c2[k]==c1[j])
			{
				f++;b[i]=c1[j];
			}
		}
		if(f==0)
		b[i]=0;
		else if(f>1)
		b[i]=-1;
	}
	fclose(p);
	p=NULL;
	p=fopen("output.txt","w");
	for(int i=0;i<t;i++)
	{
		if(b[i]==-1)
		{
			fprintf(p,"Case #%d: Bad magician!\n",i+1);
			printf("Case #%d: Bad magician!\n",i+1);
		}
		else if(b[i]==0)
		{
			fprintf(p,"Case #%d: Volunteer cheated!\n",i+1);
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
		else
		{
			fprintf(p,"Case #%d: %d\n",i+1,b[i]);
			printf("Case #%d: %d\n",i+1,b[i]);
		}
	}
	fclose(p);
	return 0;
}

