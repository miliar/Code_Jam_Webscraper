#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string s;

	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		cin>>s;
		int ans = 0;
		bool starts = false;
		if(s[0] == '-')
			starts = true;

		bool same = true;
		bool plus = true;
		for (int j = 0; j < s.length(); ++j)
		{
			if(s[j] != '-')
				same = false;

			if(s[j] != '+')
				plus = false;

			if ( !(plus || same) )
				break;
		}
		for (int j = 1; j < s.length(); ++j)
		{
			if(s[j-1] != s[j])
				ans++;
		}
		bool ends = false;
		if(s[s.length() - 1] == '+')
			ends = true;
		
		if(same)
			ans = 1;
		else if(plus)
			ans = 0;
		else if ( starts && !ends)
			ans += 1;
		else if ( !starts && !ends)
			ans++;
		
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}