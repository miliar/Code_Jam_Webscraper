#include <bits/stdc++.h>
using namespace std;

vector<string> s;


void solve(int C)
{
	map<char, int> mp;
	string in;
	vector<int>ans;
	int i, j, len;
	bool flag;

	cin>>in;

	len = in.length();
	for(i = 0 ; i < len ; i++)
	{
		if(mp.find(in[i]) == mp.end())
		{
			mp[in[i]] = 1;
		}
		else
			mp[in[i]]++;
	}

	while(mp.find('G') != mp.end())
	{
		if(mp['G'] == 0)
			break;
		ans.push_back(8);
		mp['E']--;
		mp['I']--;
		mp['G']--;
		mp['H']--;
		mp['T']--;
	}
	while(mp.find('X') != mp.end())
	{
		if(mp['X'] == 0)
			break;
		ans.push_back(6);
		mp['S']--;
		mp['I']--;
		mp['X']--;
	}

	while(mp.find('Z') != mp.end())
	{
		if(mp['Z'] == 0)
			break;
		ans.push_back(0);
		mp['Z']--;
		mp['E']--;
		mp['R']--;
		mp['O']--;
	}

	while(mp.find('U') != mp.end())
	{
		if(mp['U'] == 0)
			break;
		ans.push_back(4);
		mp['F']--;
		mp['O']--;
		mp['U']--;
		mp['R']--;
	}

	while(mp.find('W') != mp.end())
	{
		if(mp['W'] == 0)
			break;
		ans.push_back(2);
		mp['T']--;
		mp['W']--;
		mp['O']--;
	}

	while(mp.find('O') != mp.end())
	{
		if(mp['O'] == 0)
			break;
		ans.push_back(1);
		mp['O']--;
		mp['N']--;
		mp['E']--;
	}

	while(mp.find('R') != mp.end())
	{
		if(mp['R'] == 0)
			break;
		ans.push_back(3);
		mp['T']--;
		mp['H']--;
		mp['R']--;
		mp['E']--;
		mp['E']--;
	}

	while(mp.find('S') != mp.end())
	{
		if(mp['S'] == 0)
			break;
		ans.push_back(7);
		mp['S']--;
		mp['E'] -= 2;
		mp['V']--;
		mp['N']--;
	}

	while(mp.find('F') != mp.end())
	{
		if(mp['F'] == 0)
			break;
		ans.push_back(5);
		mp['F']--;
		mp['I']--;
		mp['V']--;
		mp['E']--;
	}

	while(mp.find('N') != mp.end())
	{
		if(mp['N'] == 0)
			break;
		ans.push_back(9);
		mp['N'] -= 2;
		mp['I']--;
		mp['E']--;
	}



	cout<<"Case #"<<C<<": ";
	sort(ans.begin(), ans.end());
	for(i = 0 ; i < ans.size() ; i++)
		cout<<ans[i];
	cout<<endl;
	return;
}

int main()
{
	int t;

	scanf("%d", &t);

	for(int i = 0 ; i < t ; i++)
		solve(i+1);

	return 0;
}