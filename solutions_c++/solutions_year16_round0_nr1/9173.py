#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,x;
	long long int ans;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		long long int m,n;
		cin>>m;

		int flag=1;
		if(m==0)
			cout<<"Case #"<<x<<": INSOMNIA"<<endl;
		else
		{
		int num[10]={0};
		int i=1;
		while(flag)
		{
		n=m*i;
		while(n)
		{
			num[n%10]=1;
			n/=10;
		}
		i++;
		int count=0;
		for(int j=0;j<10;j++)
		{
			count+=num[j];
		}
		if(count==10)
		{
			flag=0;
			ans=m*(i-1);
		}
		}

		cout<<"Case #"<<x<<": "<<ans<<endl;
		}
	}
	return 0;
}