#include<map>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{	
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
		int opt1;
		int a[17]={0};
		cin>>opt1;
		map<int,int>mp;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int k;
				cin>>k;
				if(i==opt1)
					mp.insert(make_pair(k,k));
			}
		}
		int opt2;
		cin>>opt2;
		int count=0,ans;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int k;
				cin>>k;
				if(i==opt2)
				{
					if(mp.find(k)!=mp.end())
					{
						count++;
						ans=k;
					}
				}
			}
		}
	
		if(count==1)
			cout<<"Case #"<<ii<<": "<<ans<<endl;
		else if(count!=0)
			cout<<"Case #"<<ii<<": "<<"Bad magician!"<<endl;
		else
			cout<<"Case #"<<ii<<": "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
