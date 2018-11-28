#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
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
#include <time.h>
#include <functional>
using namespace std;
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
const double Pi = acos(-1.0);

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MOD = 1000000007;

int a[1000007];
int n;

int f(Int x)
{
	int c = 0;
	Int s = 0;
	FOR(i,0,n)
	{
		if (s + a[i] <= x)
		{
			s += a[i];
		}
		else
		{
			if (a[i] > x)
			{
				return 7;
			}
			++c;
			s = a[i];
		}
	}
	return c;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	cin >> t;
	FOR(ttt,0,t)
	{
		int p,q,r,s;
		cin >> n >> p >> q >> r >> s;
		
		Int sum = 0;
		FOR(i,0,n)
		{
			a[i] = (1LL * i * p + q) % r + s;
			sum += a[i];
		}

		Int L = 0;
		Int R = 1000000000000000LL;
		while (R - L > 1)
		{
			Int X = (L + R) / 2;
			if (f(X) <= 2)
			{
				R = X;
			}
			else
			{
				L = X;
			}
		}
		printf("Case #%d: %.15f\n" , ttt + 1 , 1.0 * (sum - R) / sum);
	}

    return 0;
}