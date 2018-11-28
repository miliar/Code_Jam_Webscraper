// A_Mushroom Monster.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int i,j,k;
	int t,n,m[1100];
	int temp_max;
	int sum1,sum2;
	FILE *IN,*OUT;
	
	IN = fopen ("A-large.in" , "r");
	OUT = fopen ("A-large.out" , "w");
	
	fscanf(IN,"%d",&t);
	for(i=0;i<t;i++)
	{
		sum1 = 0;
		sum2 = 0;
		fscanf(IN,"%d",&n);
		for(j=0;j<n;j++)
			fscanf(IN,"%d",&m[j]);
		for(j=1;j<n;j++)
		{
			if(m[j-1]-m[j] > 0)
				sum1 = sum1 + m[j-1] - m[j];
			else{}
		}
		temp_max =-1;
		for(j=1;j<n;j++)
		{
			if (m[j-1]-m[j]>temp_max)
				temp_max = m[j-1]-m[j];
		}
		for(j=0;j<n-1;j++)
		{
			if((m[j]) >= temp_max)
				sum2 = sum2 + temp_max;
			else 
				sum2 = sum2 + m[j];

		}
		fprintf(OUT,"Case #%d: %d %d\n",i+1,sum1,sum2);
		printf("Case #%d: %d %d\n",i+1,sum1,sum2);
	}
	system("pause");
	return 0;
}

