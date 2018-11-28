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
int n, t, ans;
double a[3000], b[3000], used[3000], boo;

int main()
{
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	scanf("%d", &t);
	forn(q, t)
	{
		scanf("%d", &n);
		forn(i, n)
			scanf("%lf", &a[i]);
		forn(i, n)
			scanf("%lf", &b[i]);	
		sort(a, a + n);
		sort(b, b + n);
		ans = 0;
		forn(i, n)
			used[i] = 0;
		fornr(j, n)
		{
			boo = 0;
			fornr(i, n)
				if (!boo && !used[i] && a[i] > b[j])
					used[i] = 1, boo = 1, ans++;
			if (!boo)
				forn(i, n)
					if (!used[i])
					{
						used[i] = 0;
						break;
					}
		}
		printf("Case #%d: %d ", q + 1, ans);
		ans = 0;
		forn(i, n)
			used[i] = 0;
		fornr(i, n)
		{
			boo = 1;
			forn(j, n)
				if (boo && !used[j] && b[j] > a[i])
					used[j] = 1, boo = 0;
			ans += boo;
			if (boo)
				forn(j, n)
					if (!used[j])
					{
						used[j] = 1;
						break;
					}
		}
		printf("%d\n", ans);			
//		forn(i, n)
//			printf("%lf ", a[i]);
//		puts("");
//		forn(i, n)
//			printf("%lf ", b[i]);
//		puts("");
	}
}