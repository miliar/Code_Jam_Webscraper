#include <iostream>
#include <cassert>
#include <string>
#include <set>
#include <queue>
using namespace std;

int solveSmall(string s)
{
	set < string > used;
	queue < pair < string, int > > q;
	const string needle(s.size(), '+');
	used.insert(s);
	q.push(make_pair(s, 0));
	while (!q.empty() && q.front().first != needle)
	{
		for (int i = 1; i <= s.size(); ++i)
		{
			string s = q.front().first;
			reverse(s.begin(), s.begin() + i);
			for (int j = 0; j < i; ++j)
			{
				s[j] = s[j] == '+' ? '-' : '+';
			}
			if (!used.count(s))
			{
				used.insert(s);
				q.push(make_pair(s, q.front().second+1));
			}
		}
		q.pop();
	}
	assert(q.size());
	assert(q.front().first == needle);
	return q.front().second;
}

int main()
{
	int t;
	cin >> t;
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		string s;
		cin >> s;
		cout << "Case #" << testcase << ": " << solveSmall(s) << endl;
	}
	return 0;
}