#include<stdio.h>

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,data;
	float naomi[10000],ken[10000];
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&data);
		for(int j=0;j<data;j++)
		{
			scanf("%f",&naomi[j]);
		}
		for(int j=0;j<data;j++)
		{
			scanf("%f",&ken[j]);
		}
		float temp;
		for(int j=0;j<data-1;j++)
		{
			for(int k=j+1;k<data;k++)
			{
				if(naomi[j]>naomi[k])
				{
					temp=naomi[k];
					naomi[k]=naomi[j];
					naomi[j]=temp;
				}
			}
		}
		for(int j=0;j<data-1;j++)
		{
			for(int k=j+1;k<data;k++)
			{
				if(ken[j]>ken[k])
				{
					temp=ken[k];
					ken[k]=ken[j];
					ken[j]=temp;
				}
			}
		}
		//lie
		float temp1[10000];
		int wincount=0,tempp=0,hapus=0;
		for(int j=0;j<data;j++)
		{
			temp1[j]=ken[j];
		}
		for(int j=0;j<data;j++)
		{
			if(naomi[j]>temp1[tempp])
			{
				wincount++;
				temp1[tempp]=-1;
				tempp++;
				
			}
			else
			{
				temp1[data-1-hapus]=-1;
				hapus++;
			}
		}
		printf("Case #%d: %d",i+1,wincount);
		//truth

		for(int j=0;j<data-1;j++)
		{
			for(int k=j+1;k<data;k++)
			{
				if(naomi[j]<naomi[k])
				{
					temp=naomi[k];
					naomi[k]=naomi[j];
					naomi[j]=temp;
				}
			}
		}
		for(int j=0;j<data-1;j++)
		{
			for(int k=j+1;k<data;k++)
			{
				if(ken[j]<ken[k])
				{
					temp=ken[k];
					ken[k]=ken[j];
					ken[j]=temp;
				}
			}
		}
		wincount=0;tempp=0;hapus=0;
		for(int j=0;j<data;j++)
		{
			temp1[j]=ken[j];
		}
		for(int j=0;j<data;j++)
		{
			if(naomi[j]>temp1[tempp] && temp1[tempp]!=-1)
			{
				temp1[data-1-hapus]=-1;
				hapus++;
				wincount++;
			}
			else
			{
				temp1[tempp]=-1;
				tempp++;
				
			}
		}
		printf(" %d\n",wincount);
	}
	return 0;
}