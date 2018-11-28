#include <iostream>
using namespace std;
int *c1,*c2,count=0,count1=0,n;
void deceit(double [],double []);
void war(double [],double []);
void sort(double []);
int main() 
{
	double *arr1,*arr2;
	int t;
	cin>>t;
	for(int lol = 0;lol<t;lol++)
	{
		cin>>n;
		count=0;count1=0;
		arr1=new double[n];
		arr2=new double[n];
		c1=new int[n];
		c2=new int[n];
		for(int i=0;i<n;i++)
			cin>>arr1[i];
		for(int j=0;j<n;j++)
		{
			cin>>arr2[j];
			c1[j]=0;
			c2[j]=0;
		}
		sort(arr1);
		sort(arr2);
		deceit(arr1,arr2);
		war(arr1,arr2);
		cout<<"Case #"<<lol+1<<": ";
		cout<<count<<" "<<count1<<endl;
	}
	return 0;
}
void deceit(double arr1[],double arr2[])
{
	for(int i=0;i<n;i++)
	{
		int k1=0;
		for(int j=0;j<n;j++)
		{
			if(c2[j]==0)
			{
				if(arr1[i]>arr2[j])
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
void sort(double arr1[])
{
	int m=n-1;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			if(arr1[j]<arr1[j+1])
			{
				double t=arr1[j];
				arr1[j]=arr1[j+1];
				arr1[j+1]=t;
			}
		m--;
	}
}
void war(double arr1[],double arr2[])
{
	int k1=0,k2=9;
	for(int i=0;i<n;i++)
	{
		if(arr1[i]>arr2[k1])
		{
			count1++;
			k2--;
		}
		else
			k1++;
	}
}
