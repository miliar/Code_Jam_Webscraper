#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int cases,result1,result2;
	int arr1[4][4];
	int arr2[4][4];
	int temp1[4],temp2[4];
	int var;
	int globe=1;
	int count=0;
	int temp=-1;
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
		cin>>result1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(j==result1)
				{
					cin>>var;
					 arr1[j][k]=var;
					temp1[k]=var;
				}
				else
				cin>>arr1[j][k];
			}
		}
 
		cin>>result2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(j==result2)
				{
					cin>>var;
					 arr2[j][k]=var;
					temp2[k]=var;
				}
				else
				cin>>arr2[j][k];
			}
		}
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
	 	if(temp1[i]==temp2[j])
		{
			count++;
			temp=temp1[i];
		}
		}
	}
	if(count==1 && temp!=-1)
	{
		cout<<"Case #"<<globe++<<": "<<temp<<endl;
	}
	else if(temp==-1)
	{
		cout<<"Case #"<<globe++<<": "<<"Volunteer cheated!"<<endl;
	}
	else if(count>1)
	{
		cout<<"Case #"<<globe++<<": "<<"Bad magician!"<<endl;
	}
	count=0;
	temp=-1;
	}
	return 0;