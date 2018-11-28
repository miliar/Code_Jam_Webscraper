#include <bits/stdc++.h>

using namespace std;

map <char, int> m;

int main()
{
	int t;
	cin >> t;
	for(int c = 0; c < t; c++)
	{
		vector <int> ans;
		m.clear();
		string s;
		cin >> s;
		sort(s.begin(), s.end());
		for(int i = 0; i < s.size(); i++)
			m[s[i]]++;
		while(m['Z'] != 0)
		{
			m['Z']--;
			m['E']--;
			m['R']--;
			m['O']--;
			ans.push_back(0);
		}
		while(m['W'] != 0)
		{
			m['T']--;
			m['W']--;
			m['O']--;
			ans.push_back(2);
		}
		while(m['X'] != 0)
		{
			m['S']--;
			m['I']--;
			m['X']--;
			ans.push_back(6);
		}
		while(m['G'] != 0)
		{
			m['E']--;
			m['I']--;
			m['G']--;
			m['H']--;
			m['T']--;
			ans.push_back(8);
		}
		while(m['S'] != 0)
		{
			m['S']--;
			m['E']--;
			m['V']--;
			m['E']--;
			m['N']--;
			ans.push_back(7);
		}
		while(m['V'] != 0)
		{
			m['F']--;
			m['I']--;
			m['V']--;
			m['E']--;
			ans.push_back(5);
		}
		while(m['F'] != 0)
		{
			m['F']--;
			m['O']--;
			m['U']--;
			m['R']--;
			ans.push_back(4);
		}
		while(m['O'] != 0)
		{
			m['O']--;
			m['N']--;
			m['E']--;
			ans.push_back(1);
		}
		while(m['H'] != 0)
		{
			m['T']--;
			m['H']--;
			m['R']--;
			m['E']--;
			m['E']--;
			ans.push_back(3);
		}
		while(m['N'] != 0)
		{
			m['N']--;
			m['I']--;
			m['N']--;
			m['E']--;
			ans.push_back(9);
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << (c+1) << ": ";
		for(int i = 0; i < ans.size(); i++)
			cout << ans[i];
		cout << endl;
	}
}