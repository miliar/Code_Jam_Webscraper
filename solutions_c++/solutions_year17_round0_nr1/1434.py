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
#define MS(x, y) memset(x, y, sizeof(x))
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b > a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b < a)a = b; }
const int N = 1010, M = 0, Z = 1e9 + 7, inf = 0x3f3f3f3f;
template <class T1, class T2>inline void gadd(T1 &a, T2 b) { a = (a + b) % Z; }
int casenum, casei;
char s[N]; int K;
int main()
{
	fre();
	scanf("%d", &casenum);
	for (casei = 1; casei <= casenum; ++casei)
	{
		scanf("%s%d", s + 1, &K);
		int n = strlen(s + 1);
		int cnt = 0;
		for (int i = 1; i <= n - K + 1; ++i)if (s[i] == '-')
		{
			++cnt;
			for (int j = i; j < i + K; ++j)
			{
				s[j] = '+' + '-' - s[j];
			}
		}
		bool flag = 1;
		for (int i = n - K + 2; i <= n; ++i)if (s[i] == '-')flag = 0;
		if (!flag)printf("Case #%d: %s\n", casei, "IMPOSSIBLE");
		else printf("Case #%d: %d\n", casei, cnt);
	}
	return 0;
}
/*
��trick&&�²ۡ�


�����⡿


��������


��ʱ�临�Ӷ�&&�Ż���


*/