#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int t;
string s;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		cin >> s;
		int res = 0;
		for (int i = 1; i < s.length(); i++)
			if (s[i] != s[i - 1]) res++;
		if (s[s.length() - 1] == '-') res++;
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}