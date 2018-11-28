/*
	Time : 0347Z 20150411
	Task : GCJ 15QR B
	Tags : Enumeration
	Stat : Coding
*/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <functional>
#include <map>
#include <set>
#include <cmath>
#include <numeric>

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define fe(i,x,y) for (int i = x, y = lnk[i]; i; i = nxt[i], y = lnk[i])
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))
#define Bit(x,y) ((((x) >> (y)) & 1))
#define mit map<int,SI>::iterator
#define sit SI::iterator

using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef pair <double, double> PD;
typedef pair <LL, LL> PLI;
typedef pair <PD, int> PDI;
typedef pair <int, int> PI;
typedef pair <int, PI> PII;
typedef pair <PI, PI> PIII;
typedef set <PI> SI;
typedef vector <int> VI;
 
int Read()
{
    char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
    bool neg = (c == '-'); int ret = (neg ? 0 : c - 48);
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return neg ? -ret : ret;
}

const int MAXN = 2005;

priority_queue <int> h;
int N, a[MAXN];

int main()
{
	freopen("b.in", "r", stdin), freopen("b.out", "w", stdout);
	int cases = Read();
	fo (ca, 1, cases)
	{
		Fill(a, 0); scanf("%d", &N);
		//while (!h.empty()) h.pop();
		int ans = 0;
		fo (i, 1, N) a[i] = Read(), ans = max(ans, a[i]);
		fo (i, 1, ans)
		{
			int sum = i;
			fo (j, 1, N) sum += (a[j] - 1) / i;
			ans = min(ans, sum);
		}
		//for (int x, t = 0; h.top() > 2; x = h.top(), ans = min(ans, x + t), h.pop(), h.push(x / 2), h.push(x - x / 2), ++ t);
		/*int ans = ;
		for (;;)
		{
			int ma = 0, mb = 0, mc = 0, from = 0, zero = 0;
			fo (i, 1, N)
				if (a[i] > ma) mb = ma, ma = a[i], mc = 1;
					else if (a[i] == ma) ++ mc;
						else if (a[i] > mb) mb = a[i];
			if (!ma) break;
			mb = max(mb, ma - ma / 2);
			if (ma - mb > mc)
			{
				int n = N;
				fo (i, 1, N) if (a[i] == ma) a[++ n] = a[i] / 2, a[i] -= a[i] / 2;
				N = n, ans += mc;
			} else
			{
				ans += ma;
				break;
			}
		}*/
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0.0;
}

