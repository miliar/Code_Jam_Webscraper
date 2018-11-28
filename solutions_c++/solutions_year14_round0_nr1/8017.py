#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,r1,r2,match;
	int arr1[5][5];
	int arr2[5][5];
	for(int i=0;i<5;i++)
	{
		arr1[0][i]=0;
		arr1[i][0]=0;
			arr2[0][i]=0;
		arr2[i][0]=0;
	}
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>r1;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>arr1[i][j];
			}
		}
		cin>>r2;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>arr2[i][j];
			}
		}
		int count=0;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(arr1[r1][i]==arr2[r2][j])
				{
					count++;
					match=arr1[r1][i];
				}
			}
		}
		//cout<<count<<endl;
		if(count==0)
		{
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		}
		if(count>1)
		{
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		}
		if(count==1)
		{
			cout<<"Case #"<<k<<": "<<match<<endl;
		}
	}
	return 0;
}