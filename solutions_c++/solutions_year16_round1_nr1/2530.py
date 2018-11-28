#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define INF mod
#define pi acos(-1.0)
#define LINF 1000000000000000000LL
#define eps 1e-10

string solve(string s)
{
	if(s.size() <= 1)
		return s;
	int pos = max_element(s.begin(), s.end()) - s.begin();
	string res = solve(s.substr(0, pos));
	for(int i = pos; i < s.size(); i++)
		if(s[i] == s[pos])
			res = s[i] + res;
	for(int i = pos; i < s.size(); i++)
		if(s[i] != s[pos])
			res += s[i];
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		string res = solve(s);
		printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}