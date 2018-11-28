#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<fstream>
using namespace std;
void sorta(float arr[],int size)
{
	int i,sublist;float temp;
	
	sublist=size/2;
	for(i=0;i<size;i++)
	{
		if(sublist==1)
		break;
		if(i+sublist<size)
		{
			if(arr[i]<arr[i+sublist])
			{
				temp=arr[i];
				arr[i]=arr[i+sublist];
				arr[i+sublist]=temp;
			}
		}
		sublist=sublist/2;
	}
	for(i=0;i<size;)
	{
		if(i-1>=0)
		{
			if(arr[i]<arr[i-1])
			{
				temp=arr[i];
				arr[i]=arr[i-1];
				arr[i-1]=temp;
				i--;
			}
			else
			i++;
		}
		else
		i++;
	}
}
void sortd(float arr[],int size)
{
	int i,sublist;float temp;
	
	sublist=size/2;
	for(i=0;i<size;i++)
	{
		if(sublist==1)
		break;
		if(i+sublist<size)
		{
			if(arr[i]>arr[i+sublist])
			{
				temp=arr[i];
				arr[i]=arr[i+sublist];
				arr[i+sublist]=temp;
			}
		}
		sublist=sublist/2;
	}
	for(i=0;i<size;)
	{
		if(i-1>=0)
		{
			if(arr[i]>arr[i-1])
			{
				temp=arr[i];
				arr[i]=arr[i-1];
				arr[i-1]=temp;
				i--;
			}
			else
			i++;
		}
		else
		i++;
	}
}
int main()
{
	int t,n,na,ke,m,d=1;ofstream out;
	cin>>t;out.open("f.txt",ios::out);
	while(t--)
	{
		cin>>n;na=ke=0;
		float naomi[n],ken[n];
		for(int i=0;i<n;i++)cin>>naomi[i];
		for(int i=0;i<n;i++)cin>>ken[i];
		//qsort(naomi,n,sizeof(float),asc);
		//qsort(ken,n,sizeof(float),desc);
		sorta(naomi,n);
		sorta(ken,n);int i,j;
		for(i=0;i<n;i++)cout<<naomi[i]<<" ";
		cout<<endl;
		m=n;
		for(i=0;i<n;i++)cout<<ken[i]<<" ";
		for(i=0,j=0;i<n&&j<m;i++)
		{
			if(naomi[i]>ken[j]&&j<m){na++;j++;}
			else m--;
		}
		sorta(ken,n);
		cout<<endl<<endl;
		for(i=0;i<n;i++)cout<<naomi[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)cout<<ken[i]<<" ";
		for(i=0,j=0;i<n&&j<n;i++,j++)
		{
			while(ken[j]<naomi[i]&&j<n)j++;if(j==n)break;
		}//cout<<"i="<<i<<endl;
		ke+=n-i;
		cout<<na<<" "<<ke<<endl;
		out<<"Case #"<<d++<<": "<<na<<" "<<ke<<endl; 
	}
	return 0;
}
