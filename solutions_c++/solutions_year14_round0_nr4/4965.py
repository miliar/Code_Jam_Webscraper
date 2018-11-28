#include <stdio.h>

int main()
{
	int testCases;
	scanf("%d",&testCases);
	int t=0,i,j;
	int size;
	float naomi[10],naomid[10];
	float ken[10],kend[10];
	int dcount=0,count=0,tempCount=0;
	int countd[50],countf[50];
	while(t!=testCases)
	{
		dcount=0,count=0,tempCount=0;
		scanf("%d",&size);
		for(i=0;i<size;i++)
		{
			scanf("%f",&naomi[i]);
		}
		for(i=0;i<size;i++)
		{
			scanf("%f",&ken[i]);
		}

		for(i=0;i<size-1;i++)
		{
			for(j=0;j<size-i-1;j++)
			{
				if(naomi[j]>naomi[j+1])
				{
					float temp;
					temp=naomi[j];
					naomi[j]=naomi[j+1];
					naomi[j+1]=temp;
				}

				if(ken[j]>ken[j+1])
				{
					float temp;
					temp=ken[j];
					ken[j]=ken[j+1];
					ken[j+1]=temp;
				}
			}
		}

		for(i=0;i<size;i++)
		{
			naomid[i]=naomi[i];
			kend[i]=ken[i];
		}

		for(i=0;i<size;i++)
		{
			for(j=0;j<size;j++)
			{
				if(naomi[i]<ken[j])
				{
					if(ken[tempCount]>naomi[i])
					{
						ken[size-dcount-1]=0.0f;
						dcount++;
						break;
					}
					else if(ken[tempCount]<naomi[i])
					{
						ken[tempCount]=0.0f;
						tempCount++;
						break;
					}
				}	
			}
		}
		dcount=size-dcount;
		countd[t]=dcount;

		for(i=0;i<size;i++)
		{
			for(j=0;j<size;j++)
			{
				if(naomid[i]<kend[j])
				{
					kend[j]=0.0f;
					count++;
					break;
				}				
			}
		}
		count=size-count;
		countf[t]=count;
		t++;
	}

	for(i=0;i<testCases;i++)
	{
		printf("Case #%d: %d %d\n",i+1,countd[i],countf[i]);
	}

	while(1);
}
