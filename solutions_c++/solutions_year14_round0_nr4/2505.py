/*
ID:
PROG: spin
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
double EPS = 10e-6;
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
	//freopen("D.in", "r", stdin);
	//freopen("D.out", "w", stdout);
#endif  
}
void tme() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}

int t, n, war, d_war;
pair <double, int> a[3000];
int nayo[1111], ken[1111], nayomi_count, ken_count, nayomi_pos, ken_pos;
int was[1111];

int main() {
	ifd();

	cin >> t;
	FOR(cs, 1, t + 1) {
		cin >> n;
		FOR(i, 0, n) {
			cin >> a[i].first;
			a[i].second = 0;
		}
		FOR(i, n, 2 * n) {
			cin >> a[i].first;
			a[i].second = 1;
		}

		sort(a, a + 2 * n);

		nayomi_count = ken_count = war = d_war = nayomi_pos = ken_pos = 0;
		FOR(i, 0, 2 * n) {
			if (a[i].second == 0) {
				nayo[nayomi_count++] = i;
			}
			else {
				ken[ken_count++] = i;
			}
		}

		/*FOR(i, 0, n)
			cout << nayo[i] << " ";
		cout << endl;
		FOR(i, 0, n)
			cout << ken[i] << " ";
		cout << endl;*/

		FOR(i, 0, n) {
			if (nayo[nayomi_pos] > ken[ken_pos]) {
				d_war++;
				ken_pos++;
				nayomi_pos++;
			}
			else {
				nayomi_pos++;
			}
		}

		FOR(i, 0, n) {
			was[i] = 0;
		}
		FOR(i, 0, n) {
			int cur = nayo[i];
			int pos = -1;

			FOR(j, 0, n) {
				if (ken[j] > cur && !was[j]) {
					was[j] = 1;
					pos = j;
					break;
				}
			}
			if (pos == -1)
				war++;
		}

		printf("Case #%d: %d %d\n", cs, d_war, war);
	}

	tme();
	return 0;
}