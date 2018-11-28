#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

void exchange(double *a,double *b)
{
	double temp;
	temp = *a;
	*a = *b;
	*b = temp;
}


int Partition(double a[],int p,int r)
{
	double x = a[r];
	int i = p-1;
	int j = p;
	for(;j<=r-1;j++)
	{
		if(a[j]<x)
		{
			i+=1;
			exchange(&a[i],&a[j]);
		}
	}
	exchange(&a[i+1],&a[r]);
	return i+1;
}

void QuickSort(double a[],int p,int r)
{
	int q;
	if (p<r)
	{
		q = Partition(a,p,r);
		QuickSort(a,p,q-1);
		QuickSort(a,q+1,r);
	}
}

int main() 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

	int T;

	int N;

	int i,j,k;//for loop\

	int flag; //for find

	int resultLier;
	int result;

	int max;

#define SIZE 2000
#define MAX 1
	double naomi[SIZE];
	double ken[SIZE];

	double naomiCopy[SIZE];
	double kenCopy[SIZE];


	scanf("%d",&T);


	for(i=0;i<T;i++)
	{
		scanf("%d",&N);
		memset(naomi,0,sizeof(double)*SIZE);
		memset(ken,0,sizeof(double)*SIZE);
		
		for(j=0;j<N;j++) scanf("%lf",&naomi[j]);
		for(j=0;j<N;j++) scanf("%lf",&ken[j]);

		QuickSort(naomi,0,N-1);
		QuickSort(ken,0,N-1);

		memcpy(naomiCopy,naomi,sizeof(double)*SIZE);
		memcpy(kenCopy,ken,sizeof(double)*SIZE);

		//for(j=0;j<N;j++)
		//{
		//	printf("%lf ",naomi[j]);
		//}
		//printf("\n");

		//for(j=0;j<N;j++)
		//{
		//	printf("%lf ",ken[j]);
		//}
		//printf("\n");

		result = 0;
		resultLier = 0;

		max = 0;
		for(j=N-1;j>=0;j--)
		{
			flag = 0;
			//if(naomi[j] > ken[(N-1) - j])
			for(k=0;k<N;k++)
			{
				if(ken[k]>naomi[j])
				{
					ken[k]=-1;
					flag = 1;
					break;
				}
			}

			if(flag == 1)
			{

			}
			else
			{
				result++;
				ken[max] = -1;
				max++;
			}
		}

		memcpy(naomi,naomiCopy,sizeof(double)*SIZE);
		memcpy(ken,kenCopy,sizeof(double)*SIZE);

		max = N-1;

		//for(j=N-1;j>0;j--)
		for(j=0;j<N;j++)
		{
			flag = 0;
			//if(naomi[j] > ken[(N-1) - j])
			for(k=N-1;k>=0;k--)
			{
				if(ken[k] < naomi[j])
				{
					resultLier++;
					ken[k]= 1;
					flag = 1;
					break;
				}
			}

			if(flag == 1)
			{
				
			}
			else
			{
				//resultLier++;
				ken[max] = 1;
				max--;
			}
		}

		/*
		4
		1
		0.5
		0.6
		2
		0.7 0.2
		0.8 0.3
		3
		0.5 0.1 0.9
		0.6 0.4 0.3
		9
		0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
		0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458



		Output


		Case #1: 0 0
		Case #2: 1 0
		Case #3: 2 1
		Case #4: 8 4

		*/

		printf("Case #%d: %d %d\n",(i+1),resultLier,result);
	}
	

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  

	return 0; 
}
