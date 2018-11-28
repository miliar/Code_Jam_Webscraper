#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		int a[17]={0};
		int a1;
		cin>>a1;
		int x;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				cin>>x;
				if(j+1==a1)
				{
					a[x]++;
				}
			}
		}
		int a2;
		cin>>a2;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				cin>>x;
				if(j+1==a2)
				{
					a[x]++;
				}
			}
		}
		int ans=0;
		int val=0;
		for(int j=1;j<=16;++j)
		{
			if(a[j]>1)
			{
				ans++;
				val = j;
			}
		}
		if(ans>1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else if(ans==1)
		{
			cout<<"Case #"<<i<<": "<<val<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
