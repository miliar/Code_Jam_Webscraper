#include <bits/stdc++.h>
using namespace std;

map<string,bool> memo;

bool f(string s)
{
	if(s.size()==1)
		return true;
	if(memo.count(s))
		return memo[s];
	string t;
	for(int i=0;i<s.size();i+=2)
	{
		if(s[i]==s[i+1])
			return false;
		if(s[i]=='P' and s[i+1]=='R')
			t += 'P';
		else if(s[i+1]=='P' and s[i]=='R')
			t += 'P';
		else if(s[i]=='P' and s[i+1]=='S')
			t += 'S';
		else if(s[i+1]=='P' and s[i]=='S')
			t += 'S';
		else if(s[i]=='R' and s[i+1]=='S')
			t += 'R';
		else if(s[i+1]=='R' and s[i]=='S')
			t += 'R';
	}
	return memo[s] = f(t);
}

int main()
{
	int t;
	cin >> t;
	for(int tc=1;tc<=t;++tc)
	{
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		string str;
		while(p--)
			str += 'P';
		while(r--)
			str += 'R';
		while(s--)
			str += 'S';
		cout << "Case #" << tc << ": ";
		bool flag = false;
		do
		{
			flag = f(str);
			if(flag)
			{
				cout << str << endl;
				break;
			}
		} while(next_permutation(str.begin(),str.end()));
		if(!flag)
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
