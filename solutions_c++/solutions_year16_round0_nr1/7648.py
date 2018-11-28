#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main()
{

	vector<int> ans(1000001);
	for(int i=1;i<=1000000;i++)
	{
			
	int num=0;	
	vector<bool> cnt(10);
	bool flag=true;
		for(int j=1;j<=100000 && flag;j++)
		{
		
		long long temp=i*j;
		
		while(temp!=0)
		{
			//cout<<temp<<endl;
			int div=temp%10;
			if(!cnt[div]){
				cnt[div]=true;
				num++;
				if(num==10)
				{
					ans[i]=i*j;
					flag=false;
					break;
				}
			}	
			
			temp=temp/10;
		}	
		
		
	}
//	cout<<i<<" "<<ans[i]<<endl;
	}


	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int x;
		cin>>x;
		cout<<"Case #"<<i<<": ";
		if(x==0)
			cout<<"INSOMNIA"<<endl;
		else
			cout<<ans[x]<<endl;
	}


}

