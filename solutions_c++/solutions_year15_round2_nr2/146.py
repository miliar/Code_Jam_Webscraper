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
#include <deque>
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
//-----------------------------------------------------------

#define MAXL 10010
#define MAXC 10000000

ull R, C, N;
ull ans1, ans2;
bool** m;

ull cal() {
	ull ret = 0;
	for (ull i = 0; i < R; i++) {
		for (ull j = 1; j < C; j++) {
			if (m[i][j - 1] && m[i][j])
				ret++;
			//printf("c\n");
		}
	}

	for (ull j = 0; j < C; j++) {
		for (ull i = 1; i < R; i++) {
			if (m[i - 1][j] && m[i][j])
				ret++;
			//printf("r\n");
		}
	}

	return ret;
}

void alloc() {
	m = new bool*[R];
	for (ull i = 0; i < R; ++i)
		m[i] = new bool[C];

	for (ull i = 0; i < R; i++)
		for (ull j = 0; j < C; j++)
			m[i][j] = false;


}

void deloc() {
	for (ull i = 0; i < R; ++i) {
		delete[] m[i];
	}
	delete[] m;
}

bool putman(ull x, ull y, ull& remain, ull& ans) {
	if (m[x][y])
		return false;
	m[x][y] = true;
	remain--;
	if (remain == 0) {
		ans = cal();
		//printf("%llu\n", cal());
		deloc();
		return true;
	}
	return false;
}

void subsolve1() {

	alloc();
	ull r = N;
	// first
	for (ull i = 0; i < R; i++) {
		for (ull j = 0; j < C; j++) {
			if ((i + j) % 2 == 1) {
				if (putman(i, j, r, ans1)) return;
			}
			//printf("c\n");
		}
	}


	//second
	if (putman(0, 0, r, ans1)) return;
	if (putman(0, C - 1, r, ans1)) return;
	if (putman(R - 1, 0, r, ans1)) return;
	if (putman(R - 1, C - 1, r, ans1)) return;

	for (ull i = 0; i < R; i++) {
		if (putman(i, 0, r, ans1)) return;
		if (putman(i, C - 1, r, ans1)) return;
	}
	for (ull j = 0; j < C; j++) {
		if (putman(0, j, r, ans1)) return;
		if (putman(R - 1, j, r, ans1)) return;
	}

	for (ull i = 0; i < R; i++) {
		for (ull j = 0; j < C; j++) {
			if (putman(i, j, r, ans1)) return;
			//printf("c\n");
		}
	}
}

void subsolve2() {

	alloc();
	ull r = N;
	// first
	for (ull i = 0; i < R; i++) {
		for (ull j = 0; j < C; j++) {
			if ((i + j) % 2 == 0) {
				if (putman(i, j, r, ans2)) return;
			}
			//printf("c\n");
		}
	}


	//second
	if (putman(0, 0, r, ans2)) return;
	if (putman(0, C - 1, r, ans2)) return;
	if (putman(R - 1, 0, r, ans2)) return;
	if (putman(R - 1, C - 1, r, ans2)) return;

	for (ull i = 0; i < R; i++) {
		if (putman(i, 0, r, ans2)) return;
		if (putman(i, C - 1, r, ans2)) return;
	}
	for (ull j = 0; j < C; j++) {
		if (putman(0, j, r, ans2)) return;
		if (putman(R - 1, j, r, ans2)) return;
	}

	for (ull i = 0; i < R; i++) {
		for (ull j = 0; j < C; j++) {
			if (putman(i, j, r, ans2)) return;
			//printf("c\n");
		}
	}
}


void solve() {

	ans1 = 0;
	ans2 = 0;




	if(N == 0) {
		printf("0\n");
		return;
	}

	subsolve1();
	subsolve2();

	printf("%llu\n", min(ans1, ans2));


	fflush(stdout);

}

int main() {
	int cases;
	int caseid = 1;



	freopen("input", "r", stdin);
	//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%llu%llu%llu", &R, &C, &N);

		solve();
		//printf("%llu\n", DP(N));
	}
	return 0;
}

