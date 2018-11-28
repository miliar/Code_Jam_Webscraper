#include <iostream>
using namespace std;
int *c1,*c2,count=0,count1=0,n;
void sort(double a[])
{
	int k=n-1;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<k;j++)
		{
			if(a[j]<a[j+1])
			{
				double t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
			k--;
		}
	}
}
	
void calculationd(double a[],double b[])
{
	for(int i=0;i<n;i++)
	{
		int k1=0;
		for(int j=0;j<n;j++)
		{
			if(c2[j]==0)
			{
				if(a[i]>b[j])
				{
					c2[j]=1;
					count++;
					k1=1;
				}
			}
			if(k1==1)
			break;
		}
	}
}
void calculation(double a[],double b[])
{
	int k1=0,k2=9;
	for(int i=0;i<n;i++)
	{
		if(a[i]>b[k1])
		{
			count1++;
			k2--;
		}
		else
		k1++;
	}
}
int main() 
{	
	double *a,*b;
	int T,t,cnum=1;
	cin>>t;
	T=t;
	while(t!=0)
	{
		cin>>n;
		count=0;count1=0;
		a=new double[n];
		b=new double[n];
		c1=new int[n];
		c2=new int[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		for(int j=0;j<n;j++)
		{
			cin>>b[j];
			c1[j]=0;
			c2[j]=0;
		}
		sort(a);
		sort(b);
		calculationd(a,b);
		calculation(a,b);
		cout<<"Case #"<<cnum<<": "<<count<<" "<<count1<<endl;
		t--;
		cnum++;
	}
	return 0;
}