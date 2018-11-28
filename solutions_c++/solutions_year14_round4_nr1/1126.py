/*
ID: 
PROG: kimbits
LANG: C++
*/
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
double EPS = 10e-9;
const int INF = 2000000000;

#pragma comment(linker, "/stack:1500000000")
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
LL gcd(LL a, LL b){ if (a == 0) return b; return gcd(b%a, a); }
LL lcm(LL a, LL b){ return a / gcd(a, b) * b; }

using namespace std;

void ifd() {
#ifdef SAMMAX
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 
	beg = clock();
#else
	//freopen("kimbits.in", "r", stdin);
	//freopen("kimbits.out", "w", stdout);
#endif  
}
void tme() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}

int t, ans, p1, p2;

int n, x, a[10010];

int main() {
	ifd();

	scanf("%d", &t);

	FOR(cs, 1, t + 1) {
		ans = 0;
		scanf("%d %d", &n, &x);
		FOR(i, 0, n)
			scanf("%d", &a[i]);
		sort(a, a + n);
		p1 = 0;
		p2 = n - 1;
		
		while (1) {
			if (p1 > p2)
				break;

			int left = x - a[p2];
			ans++;
			p2--;

			if (p1 <= p2 && left >= a[p1]) {
				left -= a[p1];
				p1++;
			}
		}

		printf("Case #%d: %d\n", cs, ans);
	}
	

	tme();
	return 0;
}