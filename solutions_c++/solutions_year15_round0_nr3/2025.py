#define _CRT_SECURE_NO_DEPRECATE

#include <string>
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
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(int i=a; i<=b; i++)
#define fj(a, b) for(int j=a; j<=b; j++)
#define fo(a, b) for(int o=a; o<=b; o++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int testq;
int test;

struct num {
	short sign;
	char v;
	num operator *(const num &x) const {
		num res;
		res.sign = sign * x.sign;
		if (v == '1') {
			if (x.v == '1') {res.v = '1';}
			if (x.v == 'i') {res.v = 'i';}
			if (x.v == 'j') {res.v = 'j';}
			if (x.v == 'k') {res.v = 'k';}
		}
		if (v == 'i') {
			if (x.v == '1') {res.v = 'i';}
			if (x.v == 'i') {res.v = '1'; res.sign *= -1;}
			if (x.v == 'j') {res.v = 'k';}
			if (x.v == 'k') {res.v = 'j'; res.sign *= -1;}
		}
		if (v == 'j') {
			if (x.v == '1') {res.v = 'j';}
			if (x.v == 'i') {res.v = 'k'; res.sign *= -1;}
			if (x.v == 'j') {res.v = '1'; res.sign *= -1;}
			if (x.v == 'k') {res.v = 'i';}
		}
		if (v == 'k') {
			if (x.v == '1') {res.v = 'k';}
			if (x.v == 'i') {res.v = 'j';}
			if (x.v == 'j') {res.v = 'i'; res.sign *= -1;}
			if (x.v == 'k') {res.v = '1'; res.sign *= -1;}
		}
		return res;
	}
	bool operator==(const num &x) const {
		return sign == x.sign && v == x.v;
	}
};

#define MAX 10100

int n;
char str[MAX];
num a[MAX];

void read() {
	ZERO(a);
	ZERO(str);
	char tmp[MAX];
	int l, x;
	scanf("%d %d", &l, &x);
	scanf("%s", tmp);
	for (int i = 0; i < x; i++) {
		strcat(str, tmp);
	}
	n = l * x;
	for (int i = 0; i < n; i++) {
		a[i].sign = 1;
		a[i].v = str[i];
	}
}

num t[MAX][30];

num ONE;

num w[10000][10000];

num calc(int l, int r) {
	if (l == r) return a[l];
	if (w[l][r].v != 0) return w[l][r];
	num res = calc(l, r - 1) * a[r];
	return w[l][r] = res;
}

void solve() {
	fi(0, n - 1) {
		fj(i, n - 1) {
			w[i][j].v = 0;
		}
	}
	num I, J, K;
	I.sign = 1;
	J.sign = 1;
	K.sign = 1;
	I.v = 'i';
	J.v = 'j';
	K.v = 'k';
	fi(0, n - 1) {
		fj(i + 1, n - 2) {
			if (calc(0, i) == I && calc(i + 1, j) == J && calc(j + 1, n - 1) == K) {
				printf("YES\n");
				return;
			}
		}
	}
	printf("NO\n");
}

int main(int argc, char **argv) {
	ONE.sign = 1;
	ONE.v = '1';
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		read();
		printf("Case #%d: ", test);
		solve();
		fflush(stdout);
	}
	return 0;
}
