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

int t, ans;

int n, a[10010], b[10010], d[10010], pos_mx;

int tttt() {
	int res = 0;
	
	FOR(i, 0, n)
		d[i] = a[i];

	FOR(i, 0, n) {
		int need = b[i];
		int cur = 0;
		while (d[cur] != need) {
			cur++;
		}
		while (cur != i) {
			if (cur > i) {
				swap(d[cur], d[cur - 1]);
				cur--;
			}
			else {
				swap(d[cur], d[cur + 1]);
				cur++;
			}
			res++;
		}
	}

	return res;
}

int main() {
	ifd();

	scanf("%d", &t);

	FOR(cs, 1, t + 1) {
		ans = INT_MAX;
		pos_mx = 0;

		scanf("%d", &n);
		
		FOR(i, 0, n) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		
		sort(b, b + n);

		do {
			bool real = false;

			FOR(i, 0, n) {
				bool ok = true;

				FOR(j, 0, i)
					ok &= b[j] < b[j + 1];
				FOR(j, i, n - 1)
					ok &= b[j] > b[j + 1];

				real |= ok;
			}
			if (!real)
				continue;
			int can = tttt();
			ans = MIN(ans, can);
		} while (next_permutation(b, b + n));
		

		printf("Case #%d: %d\n", cs, ans);
	}
	

	tme();
	return 0;
}