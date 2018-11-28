#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("ans2.txt","w",stdout);
	int t;
	cin>>t;
	for(int tt=0;tt<t;tt++)
	{
		int n;
		cin>>n;
		long long int ans;
		if(n==0)
			cout<<"Case #"<<tt+1<<": "<<"INSOMNIA"<<"\n";
		else
		{
			set<int>ss;
			for(int i=1;;i++)
			{
				long long int temp=n*i*1LL;
				ans=temp;
				while(temp>0)
				{
					int x=temp%10;
					ss.insert(x);
					temp=temp/10;
				}
				if(ss.size()==10)
					break;
			}
			cout<<"Case #"<<tt+1<<": "<<ans<<"\n";
		}
	}
	return 0;
}
