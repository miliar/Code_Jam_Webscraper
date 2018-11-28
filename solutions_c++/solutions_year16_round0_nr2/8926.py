#include <iostream>
#include <set>
#include <map>
using namespace std;
int ans;
map<string, bool> m;
string flip(string s, int pos)
{
	//cerr << s << " " << pos << " ";
	for(int i = 0; i <= pos; i++)
	{
		if(s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
	for(int i = 0; i <= pos; i++)
	{
		swap(s[i], s[pos - i]);
	}
	//cerr << s << endl;
	return s;
}
int go(string s, int depth = 0)
{
	if(depth > 100)
		return 100000;
	int c = 0;
	for(int i = 0; i < s.size(); i++)
		if(s[i] == '+')
			c++;
	if(c == s.size())
		return 0;
	//cerr << s << endl;
	int mn = 1000000;
	for(int i = 0; i < s.size(); i++)
	{
		string f = flip(s, i);
		m[s] = 1;
		if(!m[f])
			mn = min(mn, go(f, depth + 1));
		m[s] = 0;
	}
	return mn + 1;
}
int main(){
	freopen("input.txt", "r", stdin);
	freopen("large_output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int k = 1; k <= T; k++)
	{
		m.clear();
		string s;
		cin >> s;
		int ans = 0;
		while(true)
		{
			int c = 0;
			for(int i = 0; i < s.size(); i++)
				if(s[i] == '+')
					c++;
			if(c == s.size())
				break;
			for(int i = s.size() - 1; i >= 0; i--)
			{
				if(s[i] == '-')
				{
					s = flip(s, i);
					ans++;
					break;
				}
			}
		}
		cout << "Case #"<< k << ": " << ans << endl;
	}
	return 0;
}