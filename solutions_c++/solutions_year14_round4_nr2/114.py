/*
* Problem: 
* Author: Leo Yu
* Time: 
* State: SOLVED
* Memo: 
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
inline int	read()
{
	int x = 0; char ch = getchar(); bool positive = 1;
	for (; ch < '0' || ch > '9'; ch = getchar())	if (ch == '-')  positive = 0;
	for (; ch >= '0' && ch <= '9'; ch = getchar())	x = x * 10 + ch - '0';
	return positive ? x : -x;
}
#define link Link
#define next Next
#define elif else if

int N, a[1005];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif

	int __ = read();
	for (int _ = 1; _ <= __; ++ _)
	{
		printf("Case #%d: ", _);
		
		N = read();
		for (int i = 1; i <= N; ++ i)	a[i] = read();
		int ans = 0;
		for (int i = 1; i <= N; ++ i)
		{
			int cnt1 = 0;
			for (int j = 1; j < i; ++ j)
				if (a[j] > a[i])	++ cnt1;
			int cnt2 = 0;
			for (int j = i + 1; j <= N; ++ j)
				if (a[j] > a[i])	++ cnt2;
			ans += min(cnt1, cnt2);
		}
		cout << ans << endl;
	}
	

	return 0;
}

