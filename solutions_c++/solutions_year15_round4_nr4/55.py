#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 16;
int m, n;

struct Field {
	int a[SIZE][SIZE];

	void Print() const {
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<m; j++)
				printf("%d", a[j][i]);
			printf("\n");
		}
		printf("\n");
	}
};

bool operator==(const Field &x, const Field &y) {
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			if (x.a[i][j] != y.a[i][j])
				return false;
	return true;
}

vector<Field> ans;

void AddAnswer(Field &f) {
	for (int s = 0; s < m; s++) {
		for (int i = 0; i < ans.size(); i++)
			if (ans[i] == f)
				return;

		for (int j = 0; j < n; j++) {
			int q = f.a[0][j];
			for (int i = 0; i < m - 1; i++)
				f.a[i][j] = f.a[i+1][j];
			f.a[m-1][j] = q;
		}
	}

	ans.push_back(f);
}


int matr[SIZE][SIZE];
int nbr[SIZE][SIZE][4];
int nall[SIZE][SIZE];

inline int fix(int x) {
	if (x < 0) x += m;
	if (x >= m) x -= m;
	return x;
}

inline bool change(int nu, int nv, int c, int sign) {
	if (nv < 0 || nv >= n) 
		return true;
	nu = fix(nu);
	nbr[nu][nv][c] += sign;
	nall[nu][nv] -= sign;
	int t = matr[nu][nv];
	if (nall[nu][nv] == 0 && t >= 0)
		return nbr[nu][nv][t] == t;
	return true;
}

void Solve(int u, int v) {
	if (u == m) {
		v++;
		u = 0;
	}
	if (v == n) {
		Field f;
		memcpy(f.a, matr, sizeof(matr));
		AddAnswer(f);
		return;
	}

	for (int c = 1; c<=3; c++) {
		matr[u][v] = c;
		bool ok = true;
		ok &= change(u, v, 0, 0);
		ok &= change(u, v-1, c, 1);
		ok &= change(u, v+1, c, 1);
		ok &= change(u-1, v, c, 1);
		ok &= change(u+1, v, c, 1);
        
		if (ok)
			Solve(u+1, v);

		matr[u][v] = -1;
		change(u, v-1, c, -1);
		change(u, v+1, c, -1);
		change(u-1, v, c, -1);
		change(u+1, v, c, -1);

	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &m);

		ans.clear();
		memset(nbr, 0, sizeof(nbr));
		memset(matr, -1, sizeof(matr));
		for (int i = 0; i<m; i++)
			for (int j = 0; j<n; j++)
				nall[i][j] = (j==0 || j==n-1) ? 3 : 4;

		Solve(0, 0);

		printf("Case #%d: %d\n", tt, ans.size());
		//for (int i = 0; i < ans.size(); i++) ans[i].Print();
		fflush(stdout);
	}
	return 0;
}
