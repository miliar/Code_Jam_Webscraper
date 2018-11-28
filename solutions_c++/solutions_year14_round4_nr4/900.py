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

int t, m, n, cnt, max_ans, ans_cnt;
string s[10];

vector <string> all[10];

int c() {
	int res = 0;
	map <string, int> lol;

	FOR(i, 0, n) {
		lol.clear();
		FOR(j, 0, all[i].size()) {
			string nw = all[i][j];
			string p = "";
			FOR(k, 0, nw.size()) {
				p += nw[k];
				lol[p]++;
			}
		}

		res += lol.size();
	}

	return res + n;
}
int main() {
	ifd();

	scanf("%d", &t);

	FOR(cs, 1, t + 1) {
		scanf("%d %d", &m, &n);
		
		max_ans = ans_cnt = 0;

		FOR(i, 0, m) {
			cin >> s[i];
		}

		cnt = 1;
		
		FOR(i, 0, m) {
			cnt *= n;
		}

		FOR(i, 0, cnt) {
			int num = i;

			FOR(j, 0, n) {
				all[j].clear();
			}

			FOR(j, 0, m) {
				all[num % n].push_back(s[j]);
				num /= n;
			}

			bool ok = true;
			FOR(j, 0, n)
				ok &= all[j].size() > 0;

			if (!ok)
				continue;

			int cur_res = c();

			max_ans = MAX(cur_res, max_ans);
		}

		FOR(i, 0, cnt) {
			int num = i;

			FOR(j, 0, n) {
				all[j].clear();
			}

			FOR(j, 0, m) {
				all[num % n].push_back(s[j]);
				num /= n;
			}

			bool ok = true;
			FOR(j, 0, n)
				ok &= all[j].size() > 0;

			if (!ok)
				continue;

			int cur_res = c();

			if (cur_res == max_ans)
				ans_cnt++;
		}

		printf("Case #%d: %d %d\n", cs, max_ans, ans_cnt);
	}


	tme();
	return 0;
}