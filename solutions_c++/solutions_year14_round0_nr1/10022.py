#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t;int k=1;
	cin>> t;	
	while(t--)
	{	int first,second,res,a[4][4],b[4][4];
		
		cin>>first;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>second;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		int count =0;
		for(int i=0;i<4;i++)
		{	
			for(int j=0;j<4;j++)
			{			
				if(a[first-1][i]==b[second-1][j])
				{	
					res = a[first-1][i];
					count++;
				}
			}
		}
	//	cout<<count<<endl;			
		if(count==1)
			{cout<<"Case #"<<k<<": "<<res<<endl;
			k++;}
		else if (count==0)
			{cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
			k++;}
		else 
			{cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
			k++;}

	}
		
	return 0;
}



			

