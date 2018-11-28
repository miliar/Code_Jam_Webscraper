#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		int n;
		cin>>n;
		int sum = 45;
		int m[10]={};
		int mult=1;
		int zero=0;
		if(n==0)
		{
			cout<<"Case #"<<cases<<": "<<"INSOMNIA\n";
			cases++;
			continue;
		}
		int chk=0;
		while(sum>0 || zero==0)
		{
			long long int q=n*mult;
			int r;
			while(q>0)
			{
				r=q%10;
				q=q/10;
				if(m[r]==0)
				{
					sum-=r;
					m[r]=1;
					if(r==0)
						zero=1;
				}
			}
			mult++;
		}
		long long int ans=n*(mult-1);
		cout<<"Case #"<<cases<<": "<<ans<<"\n";
		cases++;
	}
	return 0;
}
