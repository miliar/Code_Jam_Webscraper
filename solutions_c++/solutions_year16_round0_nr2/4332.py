#include <bits/stdc++.h>

using namespace std;

int k = 1;

void solve()
{
	string s;
	cin>>s;

	int j = s.length() - 1;

	stack<char> f;
	char c;
	int ans = 0;
	int z;
	while(j >= 0)
	{
		while(s[j] == '+')
			j--;
		if(j<0)
			break;

		if(s[0] == '-')
		{
			//whole flip
			for (int i = 0; i <= j; ++i)
			{
				f.push(s[i]);
			}
			z = 0;
			while(!f.empty())
			{
				c = f.top(); f.pop();
				if(c == '-')
					s[z] = '+';
				else
					s[z] = '-';
				z++;
			}
			ans++;
			j--;
			//cout<<"first :"<<s<<" j :"<<j<<endl;
		}
		else
		{
			int p;
			for (int i = j-1; i >= 0; --i)
			{
				if(s[i] == '+')
				{
					p = i;
					break;
				}
			}

			for (int i = 0; i <= p; ++i)
			{
				f.push(s[i]);
			}
			z = 0;
			while(!f.empty())
			{
				c = f.top(); f.pop();
				if(c == '-')
					s[z] = '+';
				else
					s[z] = '-';
				z++;
			}
			ans++;
			//cout<<"second :"<<s<<" j :"<<j<<endl;
		}
	}
	cout<<"Case #"<<k<<": "<<ans<<endl;
	k++;
}

int main()
{
	int t;
	cin>>t;

	while(t--)
		solve();
	return 0;
}