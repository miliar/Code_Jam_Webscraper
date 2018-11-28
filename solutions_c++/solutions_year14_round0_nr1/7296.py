#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,a,b,i,j,k;
	int arr[4][4];
	int array[4][4];
	int ans=0;
	int count=0;
	cin>>t;
	for(i=0;i<t;i++)
	{
		count=0;
		cin>>a;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>arr[j][k];
			}
		}
		cin>>b;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>array[j][k];
			}
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(arr[a-1][j]==array[b-1][k])
				{
					ans=arr[a-1][j];
					count++;
				}
			}
		}
		if(count==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		if(count==1)
			cout<<"Case #"<<i+1<<": "<<ans<<"\n";
		if(count>=2)
			cout<<"Case #"<<i+1<<": Bad magician!\n";
	}
}
