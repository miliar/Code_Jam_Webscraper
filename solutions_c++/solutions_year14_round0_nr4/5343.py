#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main()
{
	int t,k=1;
	cin>>t;
	while(k<=t)
	{
		int n,j,x=0;
		cin>>n;
		float *a,*b,*c;
		a=new float[n];
		b=new float[n];
		c=new float[n];
		//cout<<n<<endl;
		for(j=0;j<n;j++)
		{
			cin>>a[j];
		}
		for(j=0;j<n;j++)
		{
			cin>>b[j];
		}
		qsort(a,n,sizeof(float),compare);
		qsort(b,n,sizeof(float),compare);
		for(j=0;j<n;j++)
		{
			c[j]=a[j];
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(c[j]>b[i])
				{
					x++;
					c[j]=0;
					break;
				}
				
			}
			
		}
		cout<<"Case #"<<k<<": "<<x;
		x=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(b[j]>a[i])
				{
					x++;
					b[j]=0;
					break;
				}
				
			}
			
		}
		cout<<" "<<n-x<<"\n";
		k++;
		delete[] a;
		delete[] b;
		delete[] c;
	}
}	
			
		
