#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n;
		cin>>n;
		char c[1002];
		int a[1002];
		int sum=0;
		int diff=0;
		cin>>c;
		for(int i=0;i<=n;i++)
		{
			a[i]=c[i]-'0';
		}
		sum=a[0];
		//for(int i=0;i<=n;i++)
		//cout<<a[i]<<endl;
		for(int i=1;i<=n;i++)
		{
			if(i<=sum)
			{
				sum=sum+a[i];
			}
			if(sum<i)
			{
				diff=diff+(i-sum);
				sum=sum+a[i]+(i-sum);
			}
		}
		cout<<"Case #"<<k<<": "<<diff<<endl;

	}
}
