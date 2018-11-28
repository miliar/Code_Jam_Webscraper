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
int n, R, P, S;
struct node
{
	int v[3];
	void SORT()
	{
		sort(v, v + 3);
		reverse(v, v + 3);
	}
}T[16],tt;
pair<int,int> v[3];

void solve(int dep, int R, int P, int S)
{
	if (dep == 0)
	{
		if (R)putchar('R');
		if (P)putchar('P');
		if (S)putchar('S');
		return;
	}
	//P R S
	if (R > P && R > S || R < P && R < S)
	{
		solve(dep - 1, R / 2, P / 2 + 1, S / 2);
		solve(dep - 1, R / 2, P / 2, S / 2 + 1);
	}
	else if (P > R && P > S || P < R && P < S)
	{
		solve(dep - 1, R / 2 + 1, P / 2, S / 2);
		solve(dep - 1, R / 2, P / 2, S / 2 + 1);
	}
	else if (S > R && S > P || S < R && S < P)
	{
		solve(dep - 1, R / 2, P / 2 + 1, S / 2);
		solve(dep - 1, R / 2 + 1, P / 2, S / 2);
	}
}
int main()
{
	fre();
	T[0] = { 1,0,0 };
	T[1] = { 1,1,0 };
	for (int i = 2; i <= 12; ++i)
	{
		int x = T[i - 1].v[0] + T[i - 1].v[2];
		int y = T[i - 1].v[2] + T[i - 1].v[0];
		int z = T[i - 1].v[1] + T[i - 1].v[1];
		T[i] = { x,y,z };
		T[i].SORT();
	}
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		printf("Case #%d: ", casei);
		scanf("%d%d%d%d", &n, &R, &P, &S);
		v[0] = MP(R, 0); v[1] = MP(P, 1); v[2] = MP(S, 2);
		sort(v, v + 3); reverse(v, v + 3);
		tt = { v[0].first,v[1].first,v[2].first }; tt.SORT();
		if (tt.v[0] != T[n].v[0] || tt.v[1] != T[n].v[1] || tt.v[2] != T[n].v[2])puts("IMPOSSIBLE");
		else
		{
			solve(n, R, P, S);
			puts("");
		}
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