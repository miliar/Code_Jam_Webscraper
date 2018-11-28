#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>


#define FNAME ""

#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned long long
#define vi vector<int>
#define vvi vector<vi>
#define forn(i, n) for (int i = 0; i < n; i++)
#define fornr(i, n) for (int i = n - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = a; i < b; i++)
#define gcd __gcd
 
#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

using namespace std;

template <class T> T sqr(const T &a) {return a * a;}

int t;
double delta, x, tim, c, f, ans;

int main()
{
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	scanf("%d", &t);
	forn(q, t)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		ans = 1e9;
		delta = 2;
		tim = 0;
		ans = min(ans, tim + x / delta);
		while (delta <= 30 * x)
		{
			ans = min(ans, tim + x / delta);
			tim += c / delta;
			delta += f;		
		}
		printf("Case #%d: %.20lf\n", q + 1, ans);
	}
}
	