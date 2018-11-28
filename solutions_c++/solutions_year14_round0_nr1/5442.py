#include<iostream>
using namespace std;
int main()
{
	int t=0,r1,r2,arr1[4][4],arr2[4][4],count,result[200],x=1,s,element[100];
	cin>>t;
	s=t;
	while(t--)
	{
		count=0;
		cin>>r1;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin>>arr1[i][j];
			}
		}
		cin>>r2;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin>>arr2[i][j];
			}
		}
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				if(arr1[r1][j]==arr2[r2][i])
				{
					count++;element[x]=arr1[r1][j];
				}
			}
		}
		result[x]=count;x++;
	}
	for(int i=1;i<=s;i++)
	{
		if(result[i]==1)
		{
			cout<<"Case #"<<i<<": "<<element[i]<<"\n";
		}
		else if(result[i]==0)
		{
			cout<<"Case #"<<i<<": "<<"Volunteer cheated!\n";	
		}
		else
		{
				cout<<"Case #"<<i<<": "<<"Bad magician!\n";
		}
	}
	return 0;
}
