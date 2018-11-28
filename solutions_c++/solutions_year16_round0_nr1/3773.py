#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int it=1;it<=t;it++)
	{	
		long long int n;
		cin>>n;
		cout<<"Case #"<<it<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		long long int last_num;
		bool *digits = new bool [10];
		for(int i=0;i<10;i++)
			digits[i]=false;
		for(int i=1;i<=101;i++)
		{
			last_num = i*n;
			long long int curr=last_num;
			while(curr>0)
			{	
				digits[curr%10]=true;
				curr=curr/10;
			}
			bool flag=true;
			for(int j=0;j<10;j++)
				flag = flag && digits[j];
			if(flag)
			{
				cout<<last_num<<"\n";
				break;
			}
		}
		continue;
	}
}
