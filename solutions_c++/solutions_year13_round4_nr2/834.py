#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#include <ctime>
#include <stack>
#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

const double pi = 3.1415926535897932384626433832795;
double EPS = 10e-6;
const int INF = 2000000000;

//#pragma comment(linker, "/stack:1500000000")
#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORD(i,a,b) for (int i=(a);i>(b);--i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long
#define U unsigned
#define pnt pair <int,int>
LL gcd(LL a, LL b){if (a==0) return b;return gcd(b%a,a);}

using namespace std;

void ifd() 
{
#ifdef SAMMAX
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	beg = clock();
#else
	//freopen("spin.in", "r", stdin); 
	//freopen("spin.out", "w", stdout);
#endif	
}
void tme()
{
#ifdef SAMMAX
	fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
}

int t, n, p;
int fir[11][2000], sec[11][2000];
int main()  
{
    ifd();

	//first
	FOR(cnt, 1, 11) {
		int pos = 0, cn = (1 << cnt) / 2;
		int cur = 0, to_add = 2;
		while (cn) {
			FOR(i, 0, cn)
				fir[cnt - 1][pos++] = cur;
			cn /= 2;
			cur += to_add;
			to_add *= 2;
		}
		fir[cnt - 1][(1 << cnt) - 1] = (1 << cnt) - 1; 
	}

	//second
	FOR(cnt, 1, 11) {
		int pos = 1, cn = 2;
		int cur = (1 << cnt) / 2, to_add = cur / 2;
		while (cn < (1 << cnt)) {
			FOR(i, 0, cn)
				sec[cnt - 1][pos++] = cur;
			cn *= 2;
			cur += to_add;
			to_add /= 2;
		}
		sec[cnt - 1][(1 << cnt) - 1] = (1 << cnt) - 1; 
	}

	cin >> t;
	FOR(cs, 1, t + 1) {
		cin >> n >> p;
		printf("Case #%d: %d %d\n", cs, fir[n - 1][p - 1], sec[n - 1][p - 1]);
	}
	

	tme();
    return 0;
}
