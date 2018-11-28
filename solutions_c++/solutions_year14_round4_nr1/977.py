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
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define fornr(i, n) for (int i = n - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = a; i < (int) b; i++)
#define gcd __gcd
 
#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

using namespace std;

template <class T> T sqr(const T &a) {return a * a;}

int t, n, x, a[20000], ans, used[20000];

int main()
{
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	scanf("%d", &t);
	forn(q, t)
	{
		scanf("%d%d", &n, &x);
		forn(i, n)
			scanf("%d", &a[i]), used[i] = 0;
		ans = 0;
		sort(a, a + n);
		fornr(i, n)
			if (!used[i])
			{
			    fornr(j, i)                      
					if (!used[j] && a[i] + a[j] <= x)
					{
						used[i] = used[j] = 1;
						break;
					}
				used[i] = 1, ans++;
			}			
		printf("Case #%d: %d\n", q + 1, ans);
	}
}


	