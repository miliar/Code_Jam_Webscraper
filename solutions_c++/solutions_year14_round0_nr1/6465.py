#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int cse=1;
	while(t--)
	{
		int x,a[4],b[4],count=0,card;
		cin>>x;
		int temp;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i==x-1)
					cin>>a[j];
				else
					cin>>temp;
			}
		}
		cin>>x;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i==x-1)
					cin>>b[j];
				else
					cin>>temp;
			}
		}

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i]==b[j])
				{
					card=a[i];
					count++;
				}
			}
		}
		if(count==1)
			cout<<"Case #"<<cse<<": "<<card<<endl;
		else if(count>1)
			cout<<"Case #"<<cse<<": "<<"Bad magician!"<<endl;
		else
			cout<<"Case #"<<cse<<": "<<"Volunteer cheated!"<<endl;

		cse++;
	}
	return 0;
}
