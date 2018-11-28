#include<bits/stdc++.h>
using namespace std;
bool isTrue(int *a)
{
	for(int i=0;i<10;i++)
	{
		if(a[i]==0)
			return true;
	}
	return false;
}
int main()
{
	int t;
	cin>>t;
	int n;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		long long int num=n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		long long int m=1;
		int a[10];
		memset(a,0,sizeof(a));
		/*for(int k=0;k<10;k++)
		{
			if(a[k]!=0)
				cout<<"MEMSET FAILED";
		}*/
		while(isTrue(a))
		{
			num=n*m;
			long long int nc=num;
			while(nc)
			{
				a[nc%10]=1;
				nc/=10;
			}
			//cout<<"M = "<<m<<" NUM = "<<num<<endl;
			/*for(int k=0;k<10;k++)
				cout<<a[k]<<endl;*/
			m++;
		}
		cout<<"Case #"<<i<<": "<<n*(m-1)<<endl;
	}
	return 0;
}