#include <bits/stdc++.h>
using namespace std;
void remove(map<char, int> &m, string s, int &remaining)
{
	for (int i = 0; i < s.length(); ++i)
		m[s[i]]--;
	remaining -= s.length();
}
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		cin>>s;
		map<char, int> count;
		for (int i = 0; i < s.length(); ++i)
		{
			count[s[i]]++;
		}
		vector<int> ans;
		int remaining = s.length();
			while (count['Z'] > 0)
			{
				ans.push_back(0);
				count['Z']--; count['E']--; count['R']--; count['O']--;
				remaining -= 4;
			}
			while (count['W'] > 0)
			{
				ans.push_back(2);
				count['T']--; count['W']--; count['O']--;
				remaining -= 3;
			}
			while (count['U'] > 0)
			{
				ans.push_back(4);
				count['F']--; count['O']--; count['U']--; count['R']--;
				remaining -= 4;
			}
			while (count['X'] > 0)
			{
				ans.push_back(6);
				count['S']--; count['I']--; count['X']--; 
				remaining -= 3;
			}
			while (count['G'] > 0)
			{
				ans.push_back(8);
				remove(count, "EIGHT", remaining);
			}
			while (count['F'] > 0)
			{
				ans.push_back(5);
				remove(count, "FIVE", remaining);
			}
			while (count['V'] > 0)
			{
				ans.push_back(7);
				remove(count, "SEVEN", remaining);
			}
			while (count['R'] > 0)
			{
				ans.push_back(3);
				remove(count, "THREE", remaining);
			}
			while (count['I'] > 0)
			{
				ans.push_back(9);
				remove(count, "NINE", remaining);
			}
			while (count['N'] > 0)
			{
				ans.push_back(1);
				remove(count, "ONE", remaining);
			}
		sort(ans.begin(), ans.end());
		cout<<"Case #"<<t<<": ";
		for (int i = 0; i < ans.size(); ++i)
		{
			cout<<ans[i];
		}
		cout<<endl;
	}
}