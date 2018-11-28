#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,n,m,max1,max2,min1,min2,d,minpos;
	int **a;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d %d",&n,&m);
		a=new int*[n];
		for(int i=0;i<n;i++)
		a[i]=new int[m];
		for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		scanf("%d",&a[i][j]);
		
		for(int i=0;i<n;i++)
		{
			min1=101;
			max1=-1;
			min2=101;
			max2=-1;
			d=0;
			
			for(int j=0;j<m;j++)
			{
				if(a[i][j]<min1)
				{
					min1=a[i][j];
				}
				if(a[i][j]>max1)
				{
					max1=a[i][j];
				}
			}
			if(min1!=max1)
			for(int j=0;j<m;j++)
			if(a[i][j]==min1)
			{
				d=0;
				for(int k=0;k<n;k++)
				{
					if(a[k][j]>max2)
					max2=a[k][j];
					
				}
				if(min1==max2)
				continue;
				else
				{
					d=1;
					break;
				}
			}
			if(d==1)
			break;
			
		}
		if(d==0)
		{
			for(int i=0;i<m;i++)
			{
				min1=101;
				max1=-1;
				min2=101;
				max2=-1;
				d=0;
				
				for(int j=0;j<n;j++)
				{
					if(a[j][i]<min1)
					{
						min1=a[j][i];
					}
					if(a[j][i]>max1)
					{
						max1=a[j][i];
					}
				}
				if(min1!=max1)
				for(int j=0;j<n;j++)
				if(a[j][i]==min1)
				{
					d=0;
					for(int k=0;k<m;k++)
					{
						if(a[j][k]>max2)
						max2=a[j][k];
						
					}
					if(min1==max2)
					continue;
					else
					{
						d=1;
						break;
					}
				}
				if(d==1)
				break;
				
			}
		}
		if(d==0)
		printf("Case #%d: YES\n",i);
		else
		printf("NO\n");
		
		
	}
	return 0;
}
