#include<iostream>
using namespace std;
int main()
{
	int t,n,m;
	int one,two;
	cin>>t;
	int c=1;
	while(t--)
	{
		
		cin>>n>>m;
		int arr1[n][m];
		char arr2[n][m];
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				arr2[i][j]='f';
				
			}
		}
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>arr1[i][j];
				if(arr1[i][j]==2)
				{
					arr2[i][j]='t';
				}
			}
		}	
		
		//column wise
		for(int i=0;i<m;i++)
		{
			one=0;
			two=0;
			for(int j=0;j<n;j++)
			{
				one+=(arr1[j][i]==1) ? 1:0;
				//two+=(arr[j][i]==2) ? 1:0;
			}
			if(one==n)
			{
				for(int j=0;j<n;j++)
				{
					arr2[j][i]='t';
				}						
			}
		}
		
		//row wise
		for(int i=0;i<n;i++)
		{
			one=0;
			two=0;
			for(int j=0;j<m;j++)
			{
				one+=(arr1[i][j]==1) ? 1:0;
				//two+=(arr[j][i]==2) ? 1:0;
			}
			if(one==m)
			{
				for(int j=0;j<m;j++)
				{
					arr2[i][j]='t';
				}						
			}
		}
	
		//checking
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(arr2[i][j]=='f')
				{
					cout<<"Case #"<<c<<":"<<" NO"<<endl;
					goto A;
				}
			}
		}
		cout<<"Case #"<<c<<":"<<" YES"<<endl;
		A:;	
		
		c++;
	
	}                      //end of while loop
	return 0;
}
