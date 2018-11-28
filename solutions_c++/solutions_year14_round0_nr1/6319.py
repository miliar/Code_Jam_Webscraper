#include<iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output7.in","w",stdout);
	
	int t;
	cin>>t;
	int al=t;
	while(t--)
	{
		int arr1[4][4];
		int row1;
		cin>>row1;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr1[i][j];
			}
		}
		
		int row2;
		cin>>row2;
		int arr2[4][4];
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr2[i][j];
			}
		}
		int no;
		int count=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(arr1[row1-1][j]==arr2[row2-1][k])
				{
					no=arr1[row1-1][j];
					count++;
				}	
			}
			
		}
		if(count==0)
		cout<<"Case #"<<al-t<<": Volunteer cheated!"<<endl;
		else if(count==1)
		cout<<"Case #"<<al-t<<": "<<no<<endl;
		else
		cout<<"Case #"<<al-t<<": Bad magician!"<<endl;
		
	}
}
