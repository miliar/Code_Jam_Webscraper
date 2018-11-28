#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(true);
	int test;
	scanf("%d",&test);
	for(int t = 1; t <= test; t++)
	{
		int n;
		scanf("%d",&n);
		string s;
		cin>>s;
		int sum = s[0] - '0';
		int ans = 0;
		for(int i = 1; i < s.length(); i++)
		{
			if(sum < i)
			{
				ans += (i - sum);
				sum = i;
			}
			sum += (s[i] - '0');
		}

		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}