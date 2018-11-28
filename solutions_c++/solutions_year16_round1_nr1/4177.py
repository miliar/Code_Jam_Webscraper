#include <bits/stdc++.h>
using namespace std;

int N = 1001;

int main()
{
	int t;
	string s;
	cin >> t;
	deque<char> se;

	for (int i = 1; i <= t; ++i)
	{
		cin >> s;
		int l = s.length();
		se.push_back(s[0]);
		for(int j = 1; j < l;j++)
		{
			if(s[j] >= se.front())
				se.push_front(s[j]);
			else
				se.push_back(s[j]);
		}
		cout << "Case #" << i << ": ";
		for (int j = 0; j < l; ++j)
			cout << se[j];
		cout << endl;
		se.clear();
	}
	return 0;
}