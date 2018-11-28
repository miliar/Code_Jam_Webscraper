#include "stdio.h"
#include "iostream"

double a[1000],b[1000];

int pai(int n)
{
	int posa,posb;
	double mina,minb,tempa,tempb;
	for(int i=0;i<n;i++)
	{
		posa=i;mina=a[i];posb=i;minb=b[i];
		for(int j=i;j<n;j++)
		{
			if (a[j]<mina){posa=j;mina=a[j];}
			if (b[j]<minb){posb=j;minb=b[j];}
		}
		if(posa!=i){tempa=a[i];a[i]=a[posa];a[posa]=tempa;}
		if(posb!=i){tempb=b[i];b[i]=b[posb];b[posb]=tempb;}
	}
	return 0;
}

int war(int n)
{
	int r=0;
	int pos=0;
	for(int i=0;i<n;i++)
	{
		for(int j=pos;j<n;j++)
		{
			if(a[i]<b[j])
			{
				r++;
				pos=j+1;
				j=n;
			}
		}
	}
	return (n-r);
}

int dwar(int n)
{
	int r=0;
	int pos=0;
	for(int i=0;i<n;i++)
	{
		for(int j=pos;j<n;j++)
		{
			if(b[i]<a[j])
			{
				r++;
				pos=j+1;
				j=n;
			}
		}
	}
	return (r);
}

int main()
{
	FILE * finp;
	FILE * foutp;

	int t;
	int n;
	int rs1,rs2;

	if((finp=fopen("1.in","r"))==NULL)
	{
		printf("error");
		exit(0);
	}
	if((foutp=fopen("1.out","w"))==NULL)
	{
		printf("error");
		exit(0);
	}

	fscanf(finp,"%d",&t);

	for(int i=0;i<t;i++)
	{
		fscanf(finp,"%d",&n);
		for(int i=0;i<n;i++)fscanf(finp,"%f",&a[i]);
		for(int i=0;i<n;i++)fscanf(finp,"%f",&b[i]);
		pai(n);
		rs1=war(n);
		rs2=dwar(n);

		fprintf(foutp,"Case #%d: %d %d\n",i+1,rs2,rs1);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
