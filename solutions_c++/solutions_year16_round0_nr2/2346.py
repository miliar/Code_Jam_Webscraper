#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<t<<": ";
		int diver = 0;
		if (s.length() > 1)
		for (int i = 0; i < s.length()-1; ++i)
		{
			if (s[i] == '+' && s[i+1] == '-') diver += 2;
		}
		if (s[0] == '-') ++diver;
		cout<<diver<<'\n';
	}
}