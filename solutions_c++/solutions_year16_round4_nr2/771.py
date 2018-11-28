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
const int N = 16, M = 0, Z = 1e9 + 7, ms63 = 0x3f3f3f3f;
int casenum, casei;
int n, k;
double p[16];
int one[1 << 16];
double yes[1 << 16];
double no[1 << 16];
int main()
{
	fre();
	int top = 1 << 16;
	for (int i = 0; i < top; ++i)
	{
		for (int j = i; j; j >>= 1)one[i] += j & 1;
	}
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)scanf("%lf", &p[i]);
		int top = 1 << n;
		for (int i = 0; i < top; ++i)
		{
			yes[i] = no[i] = 1;
			for (int j = 0; j < n; ++j)if (i >> j & 1)
			{
				yes[i] = yes[i] * p[j];
				no[i] = no[i] * (1 - p[j]);
			}
		}
		double ans = 0;
		for (int i = 0; i < top; ++i)
		{
			int num = one[i]; if (num != k)continue;
			double tmp = 0;
			for (int j = i; j; j = j - 1 & i)
			{
				if (one[j] + one[j] == num)
				{
					tmp += yes[j] * no[i^j];
				}
			}
			gmax(ans, tmp);
		}
		printf("Case #%d: %.8f\n", casei, ans);
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