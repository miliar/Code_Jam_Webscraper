#include<iostream>
#include<cstdio>

using namespace std;

void split(int ms,int a[1000])
{
	
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int t=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		int ms=0;
		char c;
		int y=0;
		long long sum=0;
		cin>>ms;
		cin>>c;
		sum+=c-'0';
		for(int i=1;i<=ms;i++)
		{
			cin>>c;
			int curr=c-'0';
			if(sum>=i)
			{
				sum+=curr;
			}else if(curr>0)
			{
				y+=i-sum;
				sum=i+curr;
			}
		}
		cout<<y<<endl;
	}
	
	return 0;
}