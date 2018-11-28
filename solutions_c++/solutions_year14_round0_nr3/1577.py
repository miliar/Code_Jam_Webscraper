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


int t, r, c, m;
int desk[5][5];
int ans[6][6][30];
pnt ans2[6][6][30];
int deco[30];
int di[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dj[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
char ut[3] = { '.', '*', 'c' };

bool bfs(int si, int sj, int n, int m) {
	if (desk[si][sj])
		return false;
	
	int q[50][2], he = 0, ta = 0;
	int was[5][5], ngh[5][5];
	
	FOR(i, 0, n)
		FOR(j, 0, m)
			was[i][j] = ngh[i][j] = 0;

	FOR(i, 0, n)
		FOR(j, 0, m)
			if (desk[i][j])
				FOR(k, 0, 8)
					if (i + di[k] >= 0 && i + di[k] < n &&
						j + dj[k] >= 0 && j + dj[k] < m)
						ngh[i + di[k]][j + dj[k]]++;


	was[si][sj] = 1;
	if (ngh[si][sj] == 0) {
		q[he][0] = si;
		q[he++][1] = sj;
	}

	while (ta < he) {
		int ci = q[ta][0];
		int cj = q[ta++][1];

		FOR(i, 0, 8)
		if (ci + di[i] >= 0 && ci + di[i] < n &&
			cj + dj[i] >= 0 && cj + dj[i] < m &&
			!desk[ci + di[i]][cj + dj[i]] && !was[ci + di[i]][cj + dj[i]]) {

			was[ci + di[i]][cj + dj[i]] = 1;
			if (ngh[ci + di[i]][cj + dj[i]] == 0) {
				q[he][0] = ci + di[i];
				q[he++][1] = cj + dj[i];
			}
		}
	}

	FOR(i, 0, n)
		FOR(j, 0, m)
			if (!desk[i][j] && !was[i][j])
				return false;

	return true;
}

int main() {
	ifd();

	FOR(i, 0, 6)
		FOR(j, 0, 6)
			FOR(k, 0, 30)
				ans[i][j][k] = -1;

	FOR(side_n, 1, 6) {
		FOR(side_m, 1, 6) {
			FOR(s, 0, (1 << (side_n * side_m))) {
				int count = 0, cur = 0;
				
				FOR(i, 0, side_n * side_m) {
					if ((s >> i) & 1) {
						deco[i] = 1;
						count++;
					}
					else {
						deco[i] = 0;
					}
				}

				FOR(i, 0, side_n)
					FOR(j, 0, side_m)
						desk[i][j] = deco[cur++];

				if (ans[side_n][side_m][count] == -1) {
					FOR(i, 0, side_n)
						FOR(j, 0, side_m)
							if (bfs(i, j, side_n, side_m)) {
								ans[side_n][side_m][count] = s;
								ans2[side_n][side_m][count] = mp(i, j);
							}
				}
			}
		}
	}

	//FOR(i, 1, 6)
	//	FOR(j, 1, 6)
	//		FOR(k, 0, i*j)
	//			cout << i << " " << j << " " << k << " " << ans[i][j][k] << " " << ans2[i][j][k].first << " " << ans2[i][j][k].second << "\n";

	
	cin >> t;
	FOR(cs, 1, t + 1) {
		cin >> r >> c >> m;
		printf("Case #%d:\n", cs);
		if (ans[r][c][m] == -1) {
			printf("Impossible\n");
		}
		else {
			int cur = 0;
			FOR(i, 0, r * c) {
				if ((ans[r][c][m] >> i) & 1) {
					deco[i] = 1;
				}
				else {
					deco[i] = 0;
				}
			}

			FOR(i, 0, r)
				FOR(j, 0, c)
				desk[i][j] = deco[cur++];

			desk[ans2[r][c][m].first][ans2[r][c][m].second] = 2;

			FOR(i, 0, r) {
				FOR(j, 0, c)
					cout << ut[desk[i][j]];
				cout << endl;
			}

		}
	}

	tme();
	return 0;
}