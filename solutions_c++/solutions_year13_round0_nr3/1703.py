#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

vector <long long> ans;

bool check(long long n)
{
	char s[20];
	sprintf(s, "%lld", n);
	int l = strlen(s);
	int i;
	for (i = 0; i < l && s[i] == s[l - i - 1]; ++i);
	return i == l;
}

void solve(int t)
{
	long long a, b;
	scanf("%lld%lld", &a, &b);
	int res = 0, i;
	for (i = 0; i < ans.size(); ++i)
		if (a <= ans[i] && ans[i] <= b)
			++res;
	printf("Case #%d: %d\n", t, res);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i, T;
	for (i = 1; i <= 1e7; ++i)
		if (check(i) && check((long long)i*i))
			ans.push_back((long long)i*i);
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
		solve(i + 1);
//			printf("%d\n", i);
	return 0;
}