#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,n,m1,m2,min1,min2,n1,n2,nim1,nim2;
	FILE *p;
	p=fopen("input.txt","r");
	fscanf(p,"%d",&t);
	int y[t],z[t];
	double a[1000],b[1000],tp;
	for(int i=0;i<t;i++)
	{
		fscanf(p,"%d",&n);
		for(int j=0;j<n;j++)
		fscanf(p,"%lf",&a[j]);
		for(int j=0;j<n;j++)
		fscanf(p,"%lf",&b[j]);
		for(int k=0;k<n-1;k++)
		{
			for(int j=k+1;j<n;j++)
			{
				if(a[k]<a[j])
				{
					tp=a[k];
					a[k]=a[j];
					a[j]=tp;
				}
			}
		}
		for(int k=0;k<n-1;k++)
		{
			for(int j=k+1;j<n;j++)
			{
				if(b[k]<b[j])
				{
					tp=b[k];
					b[k]=b[j];
					b[j]=tp;
				}
			}
		}
		m1=0;
		n1=0;
		m2=0;
		n2=0;
		min1=n-1;
		nim1=n-1;
		min2=n-1;
		nim2=n-1;
		int j=0,c=0,d=0;
		while(j<n&&m1<=min1)
		{
			if(a[m1]<b[m2])
			{
				min1--;
				m2++;
			}
			else if(a[m1]>b[m2])
			{
				m1++;c++;
				m2++;
			}
			j++;
		}
		y[i]=c;
		j=0;
		while(j<n)
		{
			if(a[n1]>b[n2])
			{
				n1++;
				nim2--;d++;
			}
			else if(a[n1]<b[n2])
			{
				n1++;
				n2++;
			}
			j++;
		}
		z[i]=d;
	}
	fclose(p);
	p=fopen("output4.txt","w");
	for(int i=0;i<t;i++)
	{
		fprintf(p,"Case #%d: %d %d\n",i+1,y[i],z[i]);
		printf("Case #%d: %d %d\n",i+1,y[i],z[i]);
	}
	return 0;
}
