#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t;
	cin >>t;
	long long n;
	for(int i=1;i<=t;i++)
	{
		long long m=2;
		bool a[10];
		memset(a,false,sizeof(a));
		cin >>n;
		long long k=n;
		long long s=n;
		int count=0;
		if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			while(n)
			{
				k=n;
				while(k>0)
				{
					a[k%10]=true;
					k=k/10;
				}
				
				for(int j=0;j<10;j++)
				{
					if(a[j])
						count++;
				}
				if(count==10)
				{
					cout<<"Case #"<<i<<": "<<n<<endl;
					count=0;
					break;
				}
				n=s*m;
				m++;
				count=0;
			}
		}
	}
}
