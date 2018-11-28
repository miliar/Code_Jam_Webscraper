#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int tcase;
	int n,re1,re2,temp;
	double ken[1002],naomi[1002];
	double ken2[1002],naomi2[1002];

	FILE *in,*out;
	in=fopen("D-large.in","r");
	out=fopen("output2.txt","w");

	fscanf(in,"%d",&tcase);
	for(int t=0;t<tcase;t++)
	{
		fscanf(in,"%d",&n);
		for(int i=0;i<n;i++)
			fscanf(in,"%lf",&naomi[i]);
		for(int i=0;i<n;i++)
			fscanf(in,"%lf",&ken[i]);

		sort(&naomi[0],&naomi[n]);
		sort(&ken[0],&ken[n]);

		for(int i=0;i<n;i++)
		{
			naomi2[i]=naomi[i];
			ken2[i]=ken[i];
		}
		/*
		for(int i=0;i<n;i++)
			printf("%.3lf ",naomi[i]);
		printf("\n");
		for(int i=0;i<n;i++)
			printf("%.3lf ",ken[i]);
		printf("\n");*/

		re1=re2=0;
		for(int i=0;i<n;i++)
		{
			temp=0;
			for(int j=0;j<n;j++)
			{
				if(ken2[j]!=-1)
				{
					if(ken2[j]<naomi2[i])
					{
						temp=1;
						re1++;
						ken2[j]=-1;
						break;
					}
				}
			}
			if(temp==0)
			{
				for(int j=n-1;j>=0;j--)
				{
					if(ken2[j]!=-1)
					{
						ken2[j]=-1;
						break;
					}
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			temp=0;
			for(int j=0;j<n;j++)
			{
				if(ken[j]==-1)
					continue;
				if(ken[j]>naomi[i])
				{
					ken[j]=-1;
					temp=1;
					break;
				}
			}
			if(temp==0)
			{
				for(int j=0;j<n;j++)
				{
					if(ken[j]!=-1)
					{
						ken[j]=-1;
						break;
					}
				}
				re2++;
			}
		}
		fprintf(out,"Case #%d: %d %d\n",t+1,re1,re2);
	}
	return 0;
}