#include <iostream>
#include <string>

using namespace std;

string lastword(string s)
{
	string l = string(1, s[0]);
	for (int i = 1; i < s.length(); i++)
	{
		if (s[i] >= l[0])
			l = s[i] + l;
		else
			l = l + s[i];
	}
	return l;
}

void main()
{
	int t;
	string s;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> s;
		cout << "Case #" << i << ": " << lastword(s) << endl;
	}
}