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

int t, n, a[20000], b[20000], l, r, ans;

int main()
{
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	scanf("%d", &t);
	forn(q, t)
	{
		scanf("%d", &n);
		forn(i, n)
			scanf("%d", &a[i]), b[i] = a[i];
		l = 0, r = n - 1;
		ans = 0;
		sort(b, b + n);
		forn(i, n)
		{
			forn(j, n)
				if (a[j] == b[i])
				{
					if (j - l <= r - j)
					{
						for (int k = j; k > l; k--)
							swap(a[k], a[k - 1]), ans++;						
						l++;
					}
					else
					{
						for (int k = j; k < r; k++)
							swap(a[k], a[k + 1]), ans++;
						r--;
					
					}
					break;					
				}
		}
		printf("Case #%d: %d\n", q + 1, ans);
	}
}


