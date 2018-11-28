//#pragma comment(linker, "/stack:16777216")
#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define FILL(a,v) memset(a,v,sizeof(a))

const double PI = acos(-1.0);
const double EPS = 1e-7;

typedef long long ll;
typedef unsigned long long ull;

ll pp[] ={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
//int pp[] = {0, 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290};
int lfind(ll a)
{
	ll l = 0;
	ll r = 38;
	for (int i = 0; i < 7; ++i)
	{

		ll m = (l+r) >> 1;

		if (a < pp[m]*pp[m])
			r = m;
		else
		if (pp[m]*pp[m] < a)
			l = m;
		else
			return m;
	}
	return l;
}
int rfind(ll a)
{
	ll l = 0;
	ll r = 38;
	for (int i = 0; i < 7; ++i)
	{

		ll m = (l+r) >> 1;

		if (a < pp[m]*pp[m])
			r = m;
		else
		if (pp[m]*pp[m] < a)
			l = m;
		else
			return m;
	}
	return r;
}

void solve()
{
	ll l, r;
	scanf("%lld",&l);
	scanf("%lld",&r);

	int ll = rfind(l);
	int rr = lfind(r);
	printf("%d\n", rr-ll + 1);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	scanf("%d", &tests);
	++tests;
	for (int i = 1; i != tests; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
}





















/*
2
3
11
22
101
111
121
202
212
1001
1111
2002
10001
10101
10201
11011
11111
11211
20002
20102
3948493
5355535
554323455
677707776
691090196
803333308
886898688
*/