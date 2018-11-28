#pragma warning(disable : 4996)
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

typedef long long ll;

using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ll n = 0;
	cin >> n;
	for (int j = 1; j <= n; j++)
	{
		set<char> b;
		int x;
		cin >> x;
		if (!x) //Case #1: INSOMNIA
		{
			cout << "Case #" << j << ": INSOMNIA" << endl;
			continue;
		}
		int i;
		int  buf;
		string s;
		for (i = 1; b.size() < 10; i++)
		{
			buf = x * i;
			s = " " + buf;
			ostringstream ss;
			ss << buf;
			s = ss.str();
			for (int k = 0; k < s.size(); k++)
			{
				b.insert(s[k]);
			}
		}
		cout << "Case #" << j << ": " << buf << endl;
	}
	return 0;
}
