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
int n ,m;
int a[105][55];
int b[55][55];
int r, c;
bool okline(int o)
{
	bool flag = 1;
	if (r)for (int i = 1; i <= n; ++i)if (b[r][i]>=a[o][i])flag = 0;
	if (!flag)return 0;
	for (int i = 1; i <= n; ++i)
	{
		if (b[r + 1][i] != -1 && b[r + 1][i] != a[o][i])flag = 0;
	}
	return flag;
}
bool oklist(int o)
{
	bool flag = 1;
	if (c)for (int i = 1; i <= n; ++i)if (b[i][c]>=a[o][i])flag = 0;
	if (!flag)return 0;
	for (int i = 1; i <= n; ++i)
	{
		if (b[i][c + 1] != -1 && b[i][c + 1] != a[o][i])flag = 0;
	}
	return flag;
}
void drawline(int o)
{
	++r;
	MC(b[r], a[o]);
	
}
void drawlist(int o)
{
	++c;
	for (int i = 1; i <= n; ++i)b[i][c] = a[o][i];
}
map<int, int>mop;
map<int, int>::iterator it;
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		//步骤1，读入
		MS(a, 0);
		scanf("%d", &n);
		m = n * 2 - 1;
		mop.clear();
		for (int i = 1; i <= m; ++i)
		{
			for (int j = 1; j <= n; ++j)scanf("%d", &a[i][j]), ++mop[a[i][j]];
		}
		printf("Case #%d: ", casei);
		for (it = mop.begin(); it != mop.end(); ++it)if (it->second & 1)
		{
			printf("%d ", it->first);
		}
		puts("");
		continue;
		//步骤2，排序，使得权值按照字典序排序
		for (int i = 1; i <= m; ++i)
		{
			for (int j = m; j > i; --j)
			{
				bool flag = 0;
				for (int k = 1; k <= n; ++k)
				{
					if (a[j][k] < a[j - 1][k])
					{
						flag = 1;
						break;
					}
					else if (a[j][k] > a[j - 1][k])break;
				}
				if (flag)swap(a[j], a[j - 1]);
			}
		}
		if (casei == 16)
		{
			int pause = 1;
		}
		//步骤3，构造解
		printf("Case #%d: ", casei);
		MS(b, -1);
		r = c = 0;
		int p;
		for (int i = 1; i <= m; ++i)
		{
			int okln = okline(i);
			int okls = oklist(i);
			if (okln&&okls)
			{
				r < c ? drawline(i) : drawlist(i);
			}
			else if (okln)drawline(i);
			else if (okls)drawlist(i);
			else
			{
				//行与列都无法完成放置
				if(okline(i+1))++c, p = c+n;
				else ++r, p = r;
				--i;
			}
		}
		if (r < n)p = r + 1;
		if (c < n)p = c + 1 + n;
		if (p > n)
		{
			p -= n;
			for (int i = 1; i <= n; ++i)printf("%d ", b[i][p]);
			puts("");
		}
		else
		{
			for (int i = 1; i <= n; ++i)printf("%d ", b[p][i]);
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
100 
3
1 2 3
2 5 6
3 9 10
2 5 9
3 6 10

3
1 2 3
1 2 3
2 5 9
2 5 6
3 6 10

3
1 2 3
1 2 3
2 5 9
2 5 6
3 9 10

3
1 2 3
4 5 6
7 8 9
1 4 7
2 5 8

3
1 2 3
4 5 6
7 8 9
3 6 9
2 5 8

3
1 2 3
4 5 6
7 8 9
3 6 9
1 4 7
*/