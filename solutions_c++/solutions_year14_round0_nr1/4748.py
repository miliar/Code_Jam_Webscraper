#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int a[4][4],b[4][4],x,y,i,j,k,t,output[100],count=0,c;
	FILE *O;
	O=fopen("nik.txt","r");
	fscanf(O,"%d ",&t);
	
	for(i=0;i<t;i++)
	{
		fscanf(O,"%d",&x);
		
		for(j=0;j<4;j++)
		{
		for(k=0;k<4;k++)
		fscanf(O,"%d",&a[j][k]);
		}
		
		
		fscanf(O,"%d",&y);
		
		for(j=0;j<4;j++)
		{
		for(k=0;k<4;k++)
		fscanf(O,"%d",&b[j][k]);
		}
		
		
		count=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				
			if(a[x-1][j]==b[y-1][k])
			{
				count++;
				c=a[x-1][j];	
			}
			}
			
			
		}
		if(count==1)
		output[i]=c;
		if(count==0)
		output[i]=0;
		if(count>1)
		output[i]=-1;
		
	}
	fclose(O);
	FILE *p=NULL;
	
	p=fopen("outputjam.txt","w");
	for(i=0;i<t;i++)
	{	
		if(output[i]==-1)
		{printf("Case #%d: Bad magician!\n",i+1);
		fprintf(p,"Case #%d: Bad magician!\n",i+1);
		}
		else if(output[i]==0)
		{
		printf("Case #%d: Volunteer cheated!\n",i+1);
		fprintf(p,"Case #%d: Volunteer cheated!\n",i+1);
		}
		else
		{
		fprintf(p,"Case #%d: %d\n",i+1,output[i]);
		printf("Case #%d: %d\n",i+1,output[i]);}
	}
	fclose(p);
	
	return 0;
	
	
	
}
