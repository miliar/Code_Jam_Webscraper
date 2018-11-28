#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int t1,t2,a[4][4],b[4][4];
		cin>>t1;
		t1--;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>a[j][k];
			}
		}
		cin>>t2;
		t2--;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>b[j][k];
			}
		}
		int flag=0,temp;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[t1][j]==b[t2][k])
				{
					temp=a[t1][j];
					flag++;
				}
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<i+1<<": "<<temp<<"\n";
		}
		if(flag>1)
		{
			cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<"\n";
		}
		if(flag==0)
		{
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<"\n";
		}
	}
}
