#include<iostream>

using namespace std;

int main()
{
	int i,t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int j,k,x,y,arr[4][4],ptr[4][4];
		cin>>x;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
				cin>>arr[j][k];
		}
		cin>>y;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
				cin>>ptr[j][k];
		}
		int counts=0,ans;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(arr[x-1][j]==ptr[y-1][k])
				{
					counts++;
					ans=arr[x-1][j];
				}
			}
		}
		if(counts==0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else if(counts==1)
			cout<<"Case #"<<i<<": "<<ans<<endl;
		else
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
	}
	return 0;
}
