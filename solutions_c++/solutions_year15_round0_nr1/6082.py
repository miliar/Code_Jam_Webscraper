#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int tc = 1;
	while(tc <= t)
	{
		int n;
		scanf("%d",&n);
		string s;
		cin>>s;
		int len = s.length();
		int i = 0;
		int sum = s[0]-'0';
		int ans = 0;
		while(i < len)
		{
			i++;
			if(sum < i)
			{
				sum++;
				ans++;
			}
	//		cout<<i<<" "<<ans<<" "<<sum<<endl;
	//		i++;
			sum+=(s[i]-'0');
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
		tc++;
	}
	return 0;
}
