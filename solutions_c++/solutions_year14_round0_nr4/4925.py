#include<iostream>
using namespace std;
void sort(double arr[],int n)
{
	for(int v=1;v<n;v++)
	{
		for(int b=0;b<n-1;b++)
		{
			if(arr[b]>arr[b+1])
			{
				double temp=arr[b];
				arr[b]=arr[b+1];
				arr[b+1]=temp;
			}
		
		}
	}
}
int main()
{
	int t,n;
	cin>>t;
	int t1[t][2];
	for(int i=0;i<t;i++)
	{
		cin>>n;
		double arr1[n],arr2[n];
		for(int j=0;j<n;j++)
		{
			cin>>arr1[j];
		}
	   	for(int j=0;j<n;j++)
		{
			cin>>arr2[j];
		}
		sort(arr1,n);
	  	sort(arr2,n);
		
		int n1=0,n2=0;
		int y=0;
		int flag=0;
		int flag2=0;
		int q,p;
	 	for( p=0;p<n;p++)
		{
			for(q=y;q<n;q++)
			{
				if(arr1[p]<arr2[q])  // less condition
				{
				    y++;
				   
					break;	
				}
				else
				{
					flag++;
					y++;
				
				}
			}
			if(y==n)
			break;
		}
		int c=0;
		for( p=0;p<n;p++)
		{
			for(q=c;q<n;q++)
			{
				if(arr1[p]>arr2[q])
				{
				 
				 flag2++;
				 c++;
				break;
				
				}
			}
	    }
	    
		t1[i][0]=flag2;
		t1[i][1]=flag;
		
	
	}
	for(int j=0;j<t;j++)
	{
		cout<<"Case #"<<j+1<<": "<<t1[j][0]<<" "<<t1[j][1]<<"\n";
	}
	
}