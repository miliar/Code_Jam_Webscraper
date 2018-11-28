/*
* Problem: 
* Author: Leo Yu
* Time: 
* State: 
* Memo: 
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
inline int   read()
{
    int x = 0;  char ch = getchar(); bool positive = 1;
    for (; ch < '0' || ch > '9'; ch = getchar())  if (ch == '-')  positive = 0;
    for (; ch >= '0' && ch <= '9'; ch = getchar())    x = x * 10 + ch - '0';
    return positive ? x : -x;
}
const int N = 105;
int n, m, a[N][N], A[N], B[N];
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T = read();
	for (int t = 1; t <= T; ++ t)
	{
		n = read(), m = read();
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		for (int i = 0; i < n; ++ i)
			for (int j = 0; j < m; ++ j)
			{
				a[i][j] = read();
				A[i] = max(A[i], a[i][j]);
				B[j] = max(B[j], a[i][j]);
			}
		int flag = 1;
		for (int i = 0; i < n; ++ i)
			for (int j = 0; j < m; ++ j)
				if (a[i][j] < A[i] && a[i][j] < B[j]) flag = 0;
		printf("Case #%d: ", t);
		puts(flag ? "YES" : "NO");
	}
	return 0;
}
