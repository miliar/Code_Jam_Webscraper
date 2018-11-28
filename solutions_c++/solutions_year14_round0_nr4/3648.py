#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
void bubble_sort(double [],int);

using namespace std;


int main()
{
	int t,i,j,n,test=1;
	FILE *fp1, *fp2;
//	fp1=fopen("B-large.in", "r");
    fp1=fopen("D-large.in","r"); 
	fp2=fopen("anslarge.txt", "w");
	
	
	fscanf(fp1,"%d",&t);
	double *a,*b;
	while(t--)
	{
		
		fscanf(fp1,"%d",&n);
		a=(double*)malloc(n*sizeof(double));
		b=(double*)malloc(n*sizeof(double));
		for(i=0;i<n;i++)
		{
			fscanf(fp1,"%lf",&a[i]);
		}
		
		for(i=0;i<n;i++)
		{
			fscanf(fp1,"%lf",&b[i]);
		}
		
	
	//	bubble_sort(b,n);
	
		int flag=0;
		int x=0;
		int count=0;
		
		bubble_sort(b,n);
		sort(a,a+n);
		
		
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n-x;j++)
			{
				if(b[i]>a[j])
				{
					flag=1;
				}
				else
				{
					x++;
					flag=0;
					break;
				}
			}
			if(flag)
			{
				count++;
			}
		}
		
		
	
	   	fprintf(fp2,"Case #%d: %d ",test,n-count);
	
	
	
	
	
	
	
	
	
		bubble_sort(a,n);
	//	sort(a,a+n);
	     sort(b,b+n);
		 flag=0;
		 count=0;
		 x=0;
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n-x;j++)
			{
				if(a[i]>b[j])
				{
					flag=1;
				}
				else
				{
					x++;
					flag=0;
					break;
				}
			}
			if(flag)
			{
				count++;
			}
		}
	
			fprintf(fp2,"%d\n",count);
		
	
		
		
		

		

	
		

		
		
		test++;
	}
	
}

void bubble_sort(double list[],int n)
{
  double c, t;
  int d;
 
  for (c = 0 ; c < ( n - 1 ); c++)
  {
    for (d = 0 ; d < n - c - 1; d++)
    {
      if (list[d] < list[d+1])
      {
        /* Swapping */
 
        t         = list[d];
        list[d]   = list[d+1];
        list[d+1] = t;
      }
    }
  }
}

