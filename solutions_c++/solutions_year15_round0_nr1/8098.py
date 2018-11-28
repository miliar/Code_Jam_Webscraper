#define Yamatan_Debug 2
//#define BAYAN
#ifdef BAYAN
 #    define BAYAN_NUM "E"
#endif
 #if Yamatan_Debug == 1
 #    include <conio.h>
#endif

#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> 
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <bitset>
#include <string.h>
#include <stdio.h>

//#pragma region macros and consts

using namespace std;

typedef long long LL;
typedef unsigned long long UL2;
typedef unsigned int UNI;
typedef unsigned char UC;

#define STR(X) #X

#define ABS(a)      ((a>0)?a:-(a))
#define MIN(a,b)    ((a<b)?(a):(b))
#define MAX(a,b)    ((a<b)?(b):(a))
#define FOR(i,a,n)    for ( int i = (a); i < (n); ++i)
#define FOR_(i,a,n)		for ( int i = (a); i >= (n); --i)
#define FORI(n)        for(int i = 0; i < n; ++i)
#define MEMS(a,b)    memset(a,b,sizeof(a))

#define MP(p1, p2)      std::make_pair(p1, p2)
#define VI              std::vector<int>
#define SI              std::set<int>
#define PI				std::pair<int, int>
#define PUI				std::pair<UNI, UNI>
#define RNG(container)  container.begin(), container.end()

const int       MOD = 1000000007;
const double    EXP = 2.7182818284590452;
const double    Pi  = 3.14159265;
const double    EPS = 1e-11;
const int		INF = 1000 * 1000 * 1000;
const long long	INFL = INF * 1000 * 100;

//////////////////
//////////////////
#define MAXN 1003

int t;
int sm;
int arr[MAXN];
char c;
int res, cur;

int main(void)
{

//#pragma region macros
#if Yamatan_Debug == 2 
    freopen("A-large.in", "r", stdin); 
    freopen("A-large.out", "w", stdout);
#endif

#if Yamatan_Debug == 0
#    if defined( BAYAN )
	freopen((string(BAYAN_NUM) + string(".in")).c_str(), "r", stdin);
	freopen((string(BAYAN_NUM) + string(".txt")).c_str(), "w", stdout);
#    endif
#endif
//#pragma endregion

    // < Code here>

	cin >> t;

	FOR(tt,1,t+1)
	{
		scanf("%d%c", &sm, &c);

		FOR(i,0,sm+1)
		{
			scanf("%c", &c);
			arr[i] = c - '0';
		}

		res = 0;
		cur = arr[0];

		FOR(i,1,sm+1)
		{
			if(arr[i] != 0 && i > cur)
			{
				res += i - cur;
				cur += i - cur;
			}
				
			cur += arr[i];
		}

		printf("Case #%d: %d\n", tt, res);
	}

    // </ Code here>

#if Yamatan_Debug == 1
    _getch();
#endif

    return 0;
 }