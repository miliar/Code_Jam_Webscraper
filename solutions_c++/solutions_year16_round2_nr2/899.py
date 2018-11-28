
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
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
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXL 20
//-----------------------------------------------------------
int N, CL, JL;
int ansc, ansj, ans;
char C[MAXL], J[MAXL];
char ansC[MAXL], ansJ[MAXL];
int dc[MAXL], dj[MAXL];
int ten[] = {1, 10, 100, 1000, 10000};
void searchJ(int n, int c, int j) {
	if (n == JL) {
//		printf("%d %d, %d %d\n", c, j, abs(c - j), ans);
		if (abs(c - j) < ans) {
			ansc = c;
			ansj = j;
			ans = abs(c - j);
			strcpy(ansC, C);
			strcpy(ansJ, J);
			return;
		}
		if (abs(c - j) == ans) {
			if (c < ansc) {
				ansc = c;
				ansj = j;
				ans = abs(c - j);
				strcpy(ansC, C);
				strcpy(ansJ, J);
				return;
			}
			if (c == ansc) {
				if (j < ansj) {
					ansc = c;
					ansj = j;
					ans = abs(c - j);
					strcpy(ansC, C);
					strcpy(ansJ, J);
					return;
				}
			}
			return;
		}
//		printf("%d %d\n", c, j);
		return;
	}
	if (dj[n] == -1) {
		for (int i = 0; i < 10; i++) {
			J[JL - n - 1] = '0' + i;
			searchJ(n + 1, c, j + (i * ten[n]));
		}
	} else {
		searchJ(n + 1, c, j + (dj[n] * ten[n]));
	}
}

void searchC(int n, int c) {
	if (n == CL) {
		searchJ(0, c, 0);
		return;
	}
	if (dc[n] == -1) {
		for (int i = 0; i < 10; i++) {
			C[CL - n - 1] = '0' + i;
			searchC(n + 1, c + (i * ten[n]));
		}
	} else {
		searchC(n + 1, c + (dc[n] * ten[n]));
	}
}

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		scanf("%s%s", C, J);
		CL = strlen(C);
		JL = strlen(J);
		memset(dc, 0, sizeof(dc));
		memset(dj, 0, sizeof(dj));
		ansc = -1;
		ansj = -1;
		ans = INT_MAX;
		for (int i = 0; i < CL; i++) {
//			printf("%d => %c\n", i, C[i]);
			if (C[i] == '?') dc[CL - i - 1] = -1;
			else			 dc[CL - i - 1] = (int)(C[i] - '0');
		}
		for (int i = 0; i < JL; i++) {
			if (J[i] == '?') dj[JL - i - 1] = -1;
			else			 dj[JL - i - 1] = (int)(J[i] - '0');
		}
		searchC(0, 0);

		printf("Case #%d: %s %s", casenum++, ansC, ansJ);
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

