#include<bits/stdc++.h>
using namespace std;

int has[10]={0};
int all()
{
	for(int i=0;i<10;i++)
	{
		if(has[i]==0)
			return 0;
	}
	
		return 1;
}

void solve(long long ax)
{
	while(ax)
	{
		has[ax%10]=1;
		ax/=10;
	}
}

int main()
{
	int t;
	cin>>t;
	int t1=t;
	while(t--)
	{
		for(int i=0;i<10;i++)has[i]=0;
		long long n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<abs(t-t1)<<": "<<"INSOMNIA"<<endl;
		else{
		for(long long i=1;;i++)
		{
			if(all())
			{
				cout<<"Case #"<<abs(t-t1)<<": "<<n*(i-1)<<endl;
				break;
			}
			solve(n*i);
		}
	}

	}

	return 0;
}