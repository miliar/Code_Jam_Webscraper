// #pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <set>
#include <list>
#include <map>
#include <iterator>
#include <cstdlib>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long ll;
#define pb push_back
#define ROUND(x) round(x)
#define FLOOR(x) floor(x)
#define CEIL(x) ceil(x)
const int maxn = 1010;
const int maxm = 0;
const int inf = 0x3f3f3f3f;
const ll inf64 = 0x3f3f3f3f3f3f3f3fLL;
const double INF = 1e30;
const double eps = 1e-6;
const int P[4] = {0, 0, -1, 1};
const int Q[4] = {1, -1, 0, 0};
const int PP[8] = { -1, -1, -1, 0, 0, 1, 1, 1};
const int QQ[8] = { -1, 0, 1, -1, 1, -1, 0, 1};
int kase;
int smax;
char str[maxn];
int cnt = 0;
int ans = 0;
void init()
{
	kase++;
	cnt = ans = 0;
}
void input()
{
	scanf("%d", &smax);
	scanf("%s", str);
}
void debug()
{
	//
}
void solve()
{
	int len = strlen(str);
	for (int i = 0; i < len; i++)
	{
		int tmp = str[i] - '0';
		if (cnt < i)
		{
			ans += i - cnt;
			cnt = i;
		}
		cnt += tmp;
	}
}
void output()
{
	printf("Case #%d: %d\n", kase, ans);
}
int main()
{
	// 32-bit
	// int size = 256 << 20; // 256MB
	// char *p = (char *)malloc(size) + size;
	// __asm__("movl %0, %%esp\n" :: "r"(p));

	// 64-bit
	// int size = 256 << 20; // 256MB
	// char *p = (char *)malloc(size) + size;
	// __asm__("movq %0, %%rsp\n" :: "r"(p));

	// std::ios_base::sync_with_stdio(false);
#ifdef xysmlx
	freopen("A-large.in", "r", stdin);
	freopen("out.txt","w",stdout);
#endif

	kase = 0;
	int T;
	scanf("%d", &T);
	while (T--)
	{
		init();
		input();
		solve();
		output();
	}
	return 0;
}