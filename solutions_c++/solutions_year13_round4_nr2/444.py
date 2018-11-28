#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
//-----------------------------------------------------------

#define MODULE 1000002013ull
#define MAXN 2100
#define MOD(x) ((x)%MODULE)

struct ROUTE {
	ull begin;
	ull end;
	ull num;
	ull cost;
};

ull N, P ;

ull Search(ull t)
{
	ull ans = 0;
	ull count = 0;
	forn(i, N) {
		count = ( t & 1LL ) ? count + 1 : 0 ;
		t >>= 1 ;
	}

	forn(i, count) {
		ans = ( ans + 1 ) *2 ;
	}
	return ans ;
}

int main() {
	int cases;
	int casenum = 1;
	freopen("input", "r", stdin);
	//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {

		// input
		scanf("%llu%llu", &N, &P);
		ull All = ( (ull)1 << N);
		if ( All == P ){
			printf("Case #%d: %llu %llu\n", casenum++, P-1, P-1);
		}
		else {
			printf("Case #%d: %llu %llu\n", casenum++, Search(P-1), All - Search(All-P-1)-2);
		}
	}
	return 0;
}
