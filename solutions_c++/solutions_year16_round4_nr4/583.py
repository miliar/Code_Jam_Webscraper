#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<ctype.h>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<bitset>
#include<algorithm>
#include<time.h>
using namespace std;
void fre() { freopen("c://test//input.in", "r", stdin); freopen("c://test//output.out", "w", stdout); }
#define MS(x,y) memset(x,y,sizeof(x))
#define MC(x,y) memcpy(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b>a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b<a)a = b; }
const int N = 0, M = 0, Z = 1e9 + 7, ms63 = 0x3f3f3f3f;
int casenum, casei;
int n, m;
char a[4][4];
char b[4][4];
int c[4];
bool e[4];
bool ok(int p)
{
	if (p == n)return 1;
	int x = c[p];
	bool flag = 0;
	for (int i = 0; i < n; ++i)
	{
		if (e[i] && b[x][i] == '1')
		{
			flag = 1;
			e[i] = 0;
			if (!ok(p + 1))return 0;
			e[i] = 1;
		}
	}
	if (!flag)return 0;
}
bool check()
{
	for (int i = 0; i < n; ++i)c[i] = i;
	do
	{
		for (int i = 0; i < n; ++i)e[i] = 1;
		if (!ok(0))return 0;
	} while (next_permutation(c, c + n));
	return 1;
}
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%d", &n); m = n*n;
		for (int i = 0; i < n; ++i)scanf("%s", a[i]);
		int ans = 1e9;
		int top = 1 << m;
		for (int i = 0; i < top; ++i)
		{
			bool flag = 1;
			int cost = 0;
			MC(b, a);
			for (int j = 0; j < m; ++j)if(i>>j&1)
			{
				int y = j / n;
				int x = j % n;
				if (b[y][x] == '1')
				{
					flag = 0;
					break;
				}
				++cost;
				b[y][x] = '1';
			}
			if (cost < ans && check())
				ans = cost;
		}
		printf("Case #%d: %d\n", casei, ans);
	}
	return 0;
}
/*
【trick&&吐槽】


【题意】


【类型】


【分析】


【时间复杂度&&优化】


【数据】


*/