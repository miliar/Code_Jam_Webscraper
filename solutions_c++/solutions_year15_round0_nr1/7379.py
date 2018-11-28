#include <bits/stdc++.h>
using namespace std;

int main()
{
	std::ios::sync_with_stdio(false);
	int t;cin>>t;
	int test=1;
	while(t--)
	{
		int smax;cin>>smax;
		string str;cin>>str;
		long long sum,cnt=0;
		sum=str[0]-'0';
		for(int i=1;i<(int)str.size();i++)
		{
			if(sum<i)
			{
				cnt+=i-sum;
				sum+=i-sum;
			}
				sum+=str[i]-'0';
		}
		cout<<"Case #"<<test<<": "<<cnt<<endl;
		test++;
	}
}