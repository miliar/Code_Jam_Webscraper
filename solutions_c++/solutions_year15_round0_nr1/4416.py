#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int t,smax,sum,res;
	char s;
	cin>>t;

	for(int j=1;j<=t;j++)
	{
		res=0;
		sum=0;
		cin>>smax;
		cin>>s;
		s-='0';
		if(!s)
		{
			sum=1;
			res=1;
		}
		else sum=s;

		for(int i=1;i<=smax;i++)
		{
			if(sum<i)
			{
				res+=i-sum;
				sum=i;
			}
			cin>>s;
			s-='0';
			sum+=s;
		}

		cout<<"case #"<<j<<": "<<res<<endl;

	}

	return 0;
}