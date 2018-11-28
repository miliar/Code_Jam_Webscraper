#include <bits/stdc++.h>
using namespace std;

void query()
{
	string s;
	int k;
	cin >> s >> k;	
	vector<char> pancakes(s.size());
	for (int i=0;i<s.size();i++)
	{
		if (s[i] == '+')
		{
			pancakes[i]=1;
		} else
		{
			pancakes[i]=0;
		}
	}
	int flips=0;
	for (int i=0;i<s.size()-k+1;i++)
	{
		if (!pancakes[i])
		{
			flips++;
			for (int j=0;j<k;j++) pancakes[i+j] ^= 1;
		}
	}
	for (int i=s.size()-k;i<s.size();i++)
	{
		if (!pancakes[i])
		{
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << flips;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i=0;i<t;i++)
	{
		cout << "Case #" << i+1<< ": ";
		query();
		cout << endl;
	}
	return 0;
}
