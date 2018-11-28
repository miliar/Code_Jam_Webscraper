#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int T=t;
	while(t--)
	{
		long long int n;
		cin>>n;
		int a[11];
		for(int i=0;i<11;i++)a[i]=0;
		int count=0;
		if(n==0)
		{
			cout<<"Case #"<<T-t<<": INSOMNIA\n";
			continue;
		}
		int x = 1;
		long long int res;
		while(count < 10)
		{
			long long int op = x*n;
			res = op;
			x++; 
			while(op > 0)
			{
				int digit = op%10;
				if(a[digit]==0)
				{
					a[digit]++;
					count++;
				}
				op/=10;
			}
		}
		cout<<"Case #"<<T-t<<": "<<res<<"\n";
	}
}