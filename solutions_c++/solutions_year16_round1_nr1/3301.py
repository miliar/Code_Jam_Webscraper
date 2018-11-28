#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <set>
#include <map>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int t = 1; t <= n; t++)
	{
		string s;
		cin >> s;
		deque <char> anw;
		anw.push_back(s[0]);
		for (int i = 1; i < s.size(); i++)
		{
			if (s[i] >= anw.front()) anw.push_front(s[i]);
			else anw.push_back(s[i]);
		}
		printf("%s%d%s","Case #",t,": ");
		while (!anw.empty())
		{
			printf("%c",anw.front());
			anw.pop_front();
		}
		printf("\n");
	}
}
