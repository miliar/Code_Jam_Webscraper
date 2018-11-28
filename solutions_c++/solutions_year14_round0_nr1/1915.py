#include<cstdio>
#include<iostream>

using namespace std;

int main()
{

	int t, T;

	cin>>T;

	for(t=1;t<=T;t++)
	{
		bool Ar[17]={0};
		int i, j, temp;		
		
		int row;
		cin>>row;
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>temp;
				if(i==(row-1))
				{
					Ar[temp]=1;
				}
			}
		}
	
		int count=0, ans;
		cin>>row;
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>temp;
				if(i==(row-1) && Ar[temp]==1)
				{
					count++;
					ans = temp;
				}
			}
		}
	
		if(count == 0)
		{
			cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(count == 1)
		{
			cout<<"Case #"<<t<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
		}
		
	
	
	
	}




	return 0;
}

