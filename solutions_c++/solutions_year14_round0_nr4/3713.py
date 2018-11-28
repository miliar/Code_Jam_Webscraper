#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
void quick_sort (double *a, int n) 
{
    if (n < 2)
        return;
    double p = a[n/2];
    double *l = a;
    double *r = a+n-1;
    while (l <= r) 
	{
        if (*l<p) 
		{
			l++;
            continue;
        }
        if (*r>p) 
		{
            r--;
            continue;
        }
        double t=*l;
        *l++ = *r;
        *r-- = t;
    }
    quick_sort(a,r-a+1);
    quick_sort(l,a+n-l);
}
int main()
{
	int t,tt,i,w,dw,j;
	double n;
	double arr1[1000],arr2[1000];
	FILE *inf=fopen("D-large.in","r");
	FILE *opf=fopen("luna12.in","w+");
	fscanf(inf,"%d",&t);
	for(tt=0;tt<t;tt++)
	{
		w=0;
		fscanf(inf,"%lf",&n);
		dw=(int)n-1;
		for(i=0;i<n;i++)
		fscanf(inf,"%lf",&arr1[i]);
		for(i=0;i<n;i++)
		fscanf(inf,"%lf",&arr2[i]);
		quick_sort(arr1,n);
		quick_sort(arr2,n);
		for(j=n-1;j>=0;j--)
		{
			if(arr1[dw]>arr2[j])
			dw--;
		}
		for(j=0;j<n;j++)
		{
			if(arr1[w]<arr2[j])
			w++;
		}
		
		fprintf(opf,"Case #%d: %d %d\n",tt+1,(int)n-dw-1,(int)n-w);
	}
	return 0;
}
