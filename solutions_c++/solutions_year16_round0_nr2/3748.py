#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
string s;
int t;
bool flag;
int main ()
{
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	cin >> t;
	for(int test = 1; test <= t; ++test)
	{
		cin >> s;
		int ans = 0;
		for(int i=0;i+1<s.size();++i)
		{
			if (s[i]!=s[i+1])
				ans++;
		}
		if (s[s.size()-1]=='-') ans++;
		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}
} 