#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <map>
#include <iostream>
#include <utility>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>
#include <functional>
#include <assert.h>
#include <ctime>
#include <utility>
#include <stack>
#define SI(i) scanf("%d ", &i)
#define SII(i,j) scanf("%d%d", &i, &j)
#define SIII(i,j, k) scanf("%d%d%d", &i, &j, &k)
#define SF(i) scanf("%lf", &i)
#define SFF(i,j) scanf("%lf%lf", &i, &j)
#define SFFF(i,j, k) scanf("%lf%lf%lf", &i, &j, &k)
#define SL(i) scanf("%I64d", &i)
#define SLL(i,j) scanf("%I64d%I64d", &i, &j)
#define SLLL(i,j, k) scanf("%I64d%I64d%I64d", &i, &j, &k)
#define SS(i) scanf("%s\n", i)
#define SSS(i,j) scanf("%s %s", i, j)
#define SC(i) scanf("%d", &i)
#define SCC(i,j) scanf("%c %c\n", &i, &j)

#define PI(i) printf("%d ", i)
#define PII(i,j) printf("%d %d ", i, j)
#define PL(i) printf("%I64d ", i)
#define PLL(i,j) printf("%I64d %I64d ", i, j)
#define PS(i) printf("%s ", i)
#define PSS(i,j) printf("%s %s ", i, j)
#define PC(i) printf("%c", i)
#define PCC(i,j) printf("%c %c ", i, j)
#define PN printf("\n")
#define forin(i, k, n) for(int i = (k); i < (n); ++i)
#define forin2(i, k, n) for(int i = (k); i <= (n); ++i)
#define rforin(i, k, n) for(int i = (k); i > (n); --i)
#define mp make_pair
#define rep(i) i  < 'a' ? 'A' : 'a'
typedef unsigned long long ull;
#define pi pair<ull, ull>
using namespace std;

int t;
int main() {
#ifdef _DEBUG
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	SI(t);
	forin2(i, 1, t)
	{
		bool is[10];
		forin(j, 0, 10)
			is[j] = false;
		int cnt = 10;
		ull n, sm, tmp;
		SL(n);
		if (n == 0ll)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		sm = n;
		while (true)
		{
			tmp = sm;
			while (tmp > 0)
			{
				if (!is[tmp % 10])
				{
					is[tmp % 10] = true;
					--cnt;
				}
				tmp /= 10;
			}
			if (cnt <= 0)
				break;
			if (ULLONG_MAX - n < sm)
				return -1;
			sm += n;
		}
		printf("Case #%d: %I64d\n", i, sm);
	}
	return 0;
}