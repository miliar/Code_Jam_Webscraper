#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<assert.h>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
using namespace std;

#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define S(X) ( (X) * (X) )
#define SZ(V) (int )V.size()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)

typedef pair<int,int> PII;
typedef pair<double, double> PDD;

//typedef int LL;
typedef __int64 LL;
LL p2[100];
int N;

LL Solve1(LL sz, LL mask, LL depth, LL will_cover)
{
	assert(will_cover > 0);

	LL a, b;

	if(will_cover == sz)
	{
		a = ((p2[N-depth] - 1)<<depth) | mask;
		return a;
	}

	a = Solve1(sz/2, mask, depth+1, MIN(will_cover, sz/2));
	if(will_cover > sz/2)
	{
		b = Solve1(sz/2, mask | (1<<depth), depth+1, will_cover - sz/2);
		a = MAX(a, b);
	}

	return a;
}

LL Solve2(LL sz, LL mask, LL depth, LL will_cover)
{
	LL a, b;

	if(will_cover == sz)
	{
		return p2[N];
	}

	if(will_cover == 0)
	{
		a = mask;
		return a;
	}

	if(sz/2 <= will_cover)
	{
		a = Solve2(sz/2, mask | (1<<depth), depth+1, will_cover - sz/2);
		return a;
	}

	a = Solve2(sz/2, mask | (1<<depth), depth+1, 0);
	b = Solve2(sz/2, mask, depth+1, will_cover);
	a = MIN(a, b);
	
	return a;
}

int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	int i, ks;
	LL ans1, ans2, P;

	p2[0] = 1;
	for(i = 1; i <= 52; i++)
		p2[i] = p2[i-1]*2;

	scanf("%d", &T);
	for(ks = 1; ks <= T; ks++)
	{
		scanf("%d %I64d", &N, &P);

		ans1 = Solve2(p2[N], 0, 0, P) - 1;
		ans2 = Solve1(p2[N], 0, 0, P);

		printf("Case #%d: %I64d %I64d\n", ks, ans1, ans2);
	}

	return 0;
}
