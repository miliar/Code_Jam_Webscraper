#include<algorithm>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;


double first[1000];
double second[1000];

#if 0
void sort(double *p,int n)
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
		{
			if(p[i]>p[j])
			{
				double tmp=p[i];
				p[i]=p[j];
				p[j]=tmp;
			}
		}
}
#endif

void print(double *p, int n)
{
	int i;
	for(i=0;i<n;i++)
		printf("%lf ",p[i]);
	printf("\n");
}


int main()
{
	int testCases,k;  
	scanf("%d",&testCases);
	for(k=0;k<testCases;k++)
	{
		int n=0;
		int i,j;
		int fDW=0;
		int sDW=0;
		int fW=0;
		int sW=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&first[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&second[i]);
#if 0		
	for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
			{
				if(first[j]<first[i])
				{
					double tmp=first[i];
					first[i]=first[j];
					first[j]=tmp;
				}
			}

		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
			{
				if(second[j]<second[i])
				{
					double tmp=second[i];
					second[i]=second[j];
					second[j]=tmp;
				}
			}

#endif

		sort(first,first+n);
		sort(second,second+n);
//	 	print(first,n);		
//	 	print(second,n);		
		/*Calculate Deceitful war */
		{
		int fl=0;
		int fh=n-1;
		int sl=0;
		int sh=n-1;		
		for(i=0;i<n;i++)
		{
			if(first[fl]>second[sl])
			{
					fDW++;
					fl++;
					sl++;
			}
			else
			{
				fl++;
				sh--;
				sDW++;
			}
		}
		}	
		
		/*Calculate Deceitful war */
		{
		int fl=0;
		int fh=n-1;
		int sl=0;
		int sh=n-1;		
		for(i=0;i<n;i++)
		{
			if(second[sl]>first[fl])
			{
				//second[sl]=0;
				sW++;
				sl++;
				fl++;
			}
			else
			{
				//second[sl]=0;
				sl++;
			}
		}

		
		fW=n-sW;
		}

			printf("Case #%d: %d %d\n",k+1,fDW,fW);
		
	}
}