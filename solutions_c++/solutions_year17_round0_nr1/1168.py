#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

string s;
int l;

int solve(int idx)
{
	if(idx == s.size()) return 0;

	if(s[idx] == '+')
	{
		return solve(idx+1);
	}
	else
	{
		if(idx <= s.size() - l)
		{
			for(int i = idx ; i < idx + l ; i++)
			{
				if(s[i] == '-') s[i] = '+';
				else s[i] = '-';
			}
		}
		else{
			return -123456789;
		}
		return solve(idx+1) + 1;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);

	freopen("A-large.in", "r", stdin);
  freopen("output3.txt", "w", stdout);

	int tt;
	cin>>tt;

	for(int tc = 1; tc <= tt ; tc++)
	{
		cin>>s>>l;
		cout<<"Case #"<<tc<<": ";
		int ret = solve(0);
		if(ret < 0)
			cout<<"IMPOSSIBLE"<<'\n';
		else
			cout<<ret<<'\n';
	}
	
	return 0;
}
