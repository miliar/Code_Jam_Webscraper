#include<iostream>
using namespace std;
int main()
{
	
	int test,t=1;
	cin>>test;
	
	while(test--)
	{
		int n,m;
		cin>>n>>m;
		int a[11][11];
		
		int max=-1;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>a[i][j];
				if(a[i][j]>max)
				{
					max=a[i][j];
				}
			}
		}
		int final[11][11];//try to convert ir original from 100 mm
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{	
				final[i][j]=max;
			}
		}
		for(int i=0;i<n;i++)
		{
			//check for every elemny in row..they shoild be =
			int temp=a[i][0];
			int count=0;
			for(int j=0;j<m;j++)
			{
				if(temp!=a[i][j])
				{
					//break no need to check furthur
					break;	
				}
				else
				{
					count++;
				}
			}
			if(count==m)
			{
				//change ith row
				for(int j=0;j<m;j++)
				{
					final[i][j]=temp;
				}
			}
			
		}
		for(int j=0;j<m;j++)
		{
			int temp=a[0][j];
			int count=0;
			for(int i=0;i<n;i++)
			{
				if(temp!=a[i][j])
				{
					break;
				}
				else
				count++;
			}
			if(count==n)
			{
				for(int i=0;i<n;i++)
				{
					final[i][j]=temp;
				}
			}
		}

		int ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]!=final[i][j])
				{
					ans++;
					break;
				}
				//cout<<final[i][j]<<"\t";
			}
			if(ans!=0)
			{
				break;
			}
		}
		if(ans==0)
		{
			cout<<"Case #"<<(t++)<<": YES"<<endl;
		}
		else
		{
			cout<<"Case #"<<(t++)<<": NO"<<endl;
		}
		
	}
	return 0;
}
