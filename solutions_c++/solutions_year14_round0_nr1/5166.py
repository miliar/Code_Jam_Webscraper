#include<iostream>
using namespace std;
main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int arr[4][4], row[4], a, b;
		int count=0, ans;
		cin>>a;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>arr[j][k];
				if(j==a-1)
				row[k]=arr[j][k];
			}		
		}
		cin>>b;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>arr[j][k];
			}
		}
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(row[j]==arr[b-1][k])
				{
					count++;
					ans=row[j];
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(count==1)
		cout<<ans<<endl;
		else if(count==0)
		cout<<"Volunteer cheated!\n";
		else
		cout<<"Bad magician!\n";		
	}
}
