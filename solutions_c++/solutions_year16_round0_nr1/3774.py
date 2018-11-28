#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int i;
		cin>>i;
		bool flag[10]={false};
		int count=0;
		long long int val=i;
		while(count<10 && i!=0)
		{
			long long int temp=val;
			while(temp>0)
			{
				int index=temp%10;
				if(!flag[index])
				{
					flag[index]=true;
					count++;
				}
				temp/=10;
			}
			if(count==10)
				break;
			val+=i;
		}
		if(i==0)
			cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
		else
			cout<<"Case #"<<j<<": "<<val<<endl;
	}
	return 0;
}
