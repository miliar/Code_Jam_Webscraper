#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

string func(string &s)
{
	deque<char> d;
	string ans = s;
	d.push_back(s[0]);
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i] >= d.front())
			d.push_front(s[i]);
		else
			d.push_back(s[i]);
	}
	for (int i = 0; i < s.size(); ++i)
	{
		ans[i] = d.front();
		d.pop_front();
	}
	return ans;
}

void caseN(int i, string& s)
{
	printf("Case #%d: ", i);
	cout << func(s) << "\n";
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		string s;
		cin >> s;
		caseN(i + 1, s);
	}
	return 0;
}