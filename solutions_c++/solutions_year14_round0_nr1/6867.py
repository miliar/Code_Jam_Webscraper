#include<iostream>

using namespace std;

int main()
{	
	int t;
	cin>>t;
	int arr1[4][4],arr2[4][4],row1,row2;
	for(int q=1;q<=t;q++)
	{	
		cin>>row1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr1[i][j];
			}
		}
		cin>>row2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr2[i][j];
			}
		}
		int flag=0;
		int ans;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr1[row1-1][i]==arr2[row2-1][j])
				{
					flag++;
					ans=arr1[row1-1][i];
					continue;
				}
			}
		}
		if(flag==0)
			cout<<"Case #"<<q<<": Volunteer cheated!"<<endl;
		else if(flag==1)
			cout<<"Case #"<<q<<": "<<ans<<endl;
		else
			cout<<"Case #"<<q<<": Bad magician!"<<endl;
	}
	return 0;
}
