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
#include <limits.h>
//#include <unordered_map>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
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
#define PL				std::pair<LL, LL>
#define PUI				std::pair<UNI, UNI>
#define RNG(container)  container.begin(), container.end()
#define endl			"\n"

const int       MOD = 1000000007;
const double    EXP = 2.7182818284590452;
const double    Pi = 3.1415926535;
const long double    EPS = 1e-9;
const int		INF = 1000 * 1000 * 1001;
const long long	INFL = (LL)INF * (LL)INF;

//map< pair<LL, LL>, LL > hashgcd;

LL gcd(LL a, LL b)
{
	if (a < b) swap(a, b);

	//	if (hashgcd.find(MP(a, b)) != hashgcd.end())
	//		return hashgcd[MP(a, b)];

	while (b != 0)
	{
		a %= b;
		swap(a, b);
	}

	//	hashgcd[MP(a, b)] = a;

	return a;
}

LL lcm(LL a, LL b)
{
	return (a / gcd(a, b)) * b;
}

LL extgcd(LL a, LL b, LL & x, LL & y)
{
	if (a == 0)
	{
		x = 0; y = 1;
		return b;
	}

	LL x11, y11;
	LL d = extgcd(b % a, a, x11, y11);
	x = y11 - (b / a) * x11;
	y = x11;
	return d;
}

ULL poww(ULL v, ULL p, ULL mod)
{
	if (p == 0) return 1;

	if (p & 1)
	{
		return (poww(v, p - 1, mod) * v) % mod;
	}
	else
	{
		ULL t = poww(v, p / 2, mod);
		return (t * t) % mod;
	}
}

const ULL L31018 = 3000000000000000000L;
const ULL L1018 = 1000000000000000000L;

//////////////////
//////////////////
#define MAXN 2003

int t;
char buf[MAXN];

int arr[26], l, cur;

int ph[MAXN];

void add(int d)
{
	ph[cur] = d;
	++cur;
}

void calc(int d, int ch, const char* rmv)
{
 	int l = strlen(rmv);

	while (arr[ch])
	{		
		add(d);

		FOR(i, 0, l)
		{
			--arr[rmv[i] - 'A'];
		}
	}
}

void accept()
{
	cin >> t;

	FOR(k, 1, t + 1)
	{
		scanf("%s", buf);
		cur = 0;
		l = strlen(buf);

		FOR(i, 0, l)
			++arr[buf[i] - 'A' - 0];

		calc(0, 'Z' - 'A', "ZERO");
		calc(2, 'W' - 'A', "TWO");
		calc(8, 'G' - 'A', "EIGHT");
		calc(3, 'T' - 'A', "THREE");
		calc(4, 'R' - 'A', "FOUR");
		calc(5, 'F' - 'A', "FIVE");
		calc(6, 'X' - 'A', "SIX");
		calc(7, 'V' - 'A', "SEVEN");		
		calc(1, 'O' - 'A', "ONE");
		calc(9, 'I' - 'A', "NINE");

		sort(ph, ph + cur);

		FOR(i, 0, 26)
			arr[i] = 0;

		printf("Case #%d: ", k);

		FOR(i, 0, cur)
			printf("%d", ph[i]);

		printf("\n");
	}
}

//		||
//		||
//     \||/
//    \\||//
//   \\\\////
//    \\\///
//     \\//
//      \/


const char inputFile[] = "busy_day.in";

int main(void)
{

#if Debug
	LL startTime = clock();
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//	freopen("cinema.in", "r", stdin);
	//	freopen("cinema.out", "w", stdout);
#endif

	//	test();
	accept();

#if Debug
	printf("\n\n\t TIME: %.5lf", double((clock() - startTime)) / 1000.0f); /// CLOCKS_PER_SEC));
	int l;
	cin >> l;
	//	_getch();
#endif
	return 0;
}