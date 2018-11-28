#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define PI 3.14159265359
#define endl '\n'

using namespace std;

int test;

inline bool f(string const& s)
{
	for(char c : s)
		if(c == '-')
			return 0;
	return 1;
}

void g(string &s,int x)
{
	for(int i=0;2*i<x;i++)
	{
		char temp = s[x-i-1];
		s[x-i-1] = (s[i] == '-' ? '+' : '-');
		s[i] = (temp == '-' ? '+' : '-');
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	
	cin >> test;
	for(int te=1;te<=test;te++)
	{
		string s;
		cin >> s;
		
		int ans = 0,n = s.size();
		while(!f(s))
		{
			if(s[0] == '+')
			{
				int cur = 0;
				while(s[cur] == '+')
					++cur;
				g(s,cur);
				++ans;
			}
			if(f(s))
				break;
			int cur = n-1;
			++ans;
			while(cur >= 0 && s[cur] == '+')
				--cur;
			if(cur == -1)
				break;
			g(s,cur+1);
		}
		
		cout << "Case #" << te << ": " << ans << endl;
	}
	
	return 0;
}