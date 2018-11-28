#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

#define vt vector
#define ll long long

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		string s, s1;
		cin >> s;
		s1 = "";
		for (int i = 0; i < s.length(); i++)
			if (i == 0)
				s1 += s[0];
			else
			{
				if (s[i] >= s1[0])
					s1 = s[i] + s1;
				else
					s1 += s[i];
			}
		cout << "Case #" << cases << ": " << s1 << endl;
	}
	return 0;
}