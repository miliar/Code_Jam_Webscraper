#include "stdio.h"
#include "iostream"


int main()
{
	FILE * finp;
	FILE * foutp;

	int t,rs;
	int m,n;
	int a[4],b[4],c[4];
	int temp,pos;

	if((finp=fopen("A-small-attempt0.in","r"))==NULL)
	{
		printf("error");
		exit(0);
	}
	if((foutp=fopen("A-small-attempt0.out","w"))==NULL)
	{
		printf("error");
		exit(0);
	}

	fscanf(finp,"%d",&t);

	for(int i=0;i<t;i++)
	{
		fscanf(finp,"%d",&m);
		for(int i=0;i<m;i++)
			fscanf(finp,"%d%d%d%d",a,a+1,a+2,a+3);
		for(int i=m;i<4;i++)
			fscanf(finp,"%d%d%d%d",c,c+1,c+2,c+3);
		fscanf(finp,"%d",&n);
		for(int i=0;i<n;i++)
			fscanf(finp,"%d%d%d%d",b,b+1,b+2,b+3);
		for(int i=n;i<4;i++)
			fscanf(finp,"%d%d%d%d",c,c+1,c+2,c+3);
		temp=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				if ( a[i]==b[j] ) {temp++;pos=i;}
		}
		if(temp>1) 
		fprintf(foutp,"Case #%d: Bad magician!\n",i+1);
		if(temp==0) 
		fprintf(foutp,"Case #%d: Volunteer cheated!\n",i+1);
		if(temp==1)
		{
			fprintf(foutp,"Case #%d: %d\n",i+1,a[pos]);
		}
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
