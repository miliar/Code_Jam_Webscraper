#include<iostream>
#include<vector>
using namespace std;

int check(vector<int> t)
{
	for(int i=0;i<10;i++)
	{
		if(t[i]==0)
			return 1;
	}
	return 0;
}

int main()
{
	int t;
	long n;
	cin>>t;
	int case1=0;
	while(t-->0)
	{
		case1++;
		vector<int> hash(10,0);
		cin>>n;
		int flag=0;
		long long z;
		if(n==0)
		{
			cout<<"Case #"<<case1<<": "<<"INSOMNIA"<<endl;
			//for(int j=0;j<10;j++)
		//		cout<<hash[j]<<" ";
		//	cout<<endl;
			continue;
		}
		for(int i=1;;i++)
		{
			z=n*i;
			
			//cout<<z<<" ";
			int x=z;
			while(x!=0)
			{
				int temp=x%10;
				x/=10;
				hash[temp]+=1;
			}
			//cout<<z<<endl;
			if(check(hash)==0)
			{

				cout<<"Case #"<<case1<<": "<<z<<endl;
		//		for(int j=0;j<10;j++)
		//			cout<<hash[j]<<" ";
		//		cout<<endl;
				break;
			}
			if(i==500)
			{
				cout<<"Case #"<<case1<<": "<<"INSOMNIA"<<endl;
				break;
			}
		}
	}
}