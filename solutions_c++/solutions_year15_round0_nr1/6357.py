#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int sm;
	string s;
	int sum;
	int ans;
	for(int it=1;it<=t;it++)
	{
		sum=0;
		ans=0;
		cin>>sm;
		cin>>s;
		sum=(int)(s[0]-'0');
		for(int i=1;i<=sm;i++)
		{
			int p=(int)(s[i]-'0');
			if(i>sum)
			{
				int ext=i-sum;
				ans+=ext;
				sum+=ext;
			}
			sum+=p;
		}
		cout<<"Case #"<<it<<":"<<" "<<ans<<endl;
	}
	return 0;
}