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

int t, x, a[4][4], b[4][4], y, used[30], boo;

int main()
{
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	scanf("%d", &t);
	forn(q, t)
	{
		scanf("%d", &x);
		forn(i, 4)
			forn(j, 4)
				scanf("%d", &a[i][j]);
		scanf("%d", &y);
		forn(i, 4)
			forn(j, 4)
				scanf("%d", &b[i][j]);
		x--, y--;
		forn(i, 20)
			used[i] = 0;
		printf("Case #%d: ", q + 1);
		boo = 0;
		forn(i, 4)
			used[a[x][i]]++, used[b[y][i]]++;
		forn(i, 20)
		{
			if (boo && used[i] == 2)
			{
				puts("Bad magician!");
			    boo = 239;
				break;
			}
	    	if (used[i] == 2)
	    		boo = i;
		}
		if (!boo)
			puts("Volunteer cheated!");
		else if (boo != 239)
			printf("%d\n", boo);			
	}
}
	