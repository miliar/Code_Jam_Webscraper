#include<time.h>
#include<stdlib.h>
#include<assert.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<map>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define rep(i,l,r) for(int i=l;i<r;i++)
#define abs(x) ((x)<(0)?(-x):(x))
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define de(x) cout << #x << " = " << x << endl;
#define local(x) freopen(x".in", "r", stdin);
#define setIO(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout);
const int N = 2e2 + 7;
const int INF = 2e9 + 7;
const int MOD = 1e9 + 7;
const ll LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-9;
void swap(int &a, int &b) {
	int t = a;
	a = b;
	b = t;
}
void gao(int a, int b, int c) {
	int a1, b1, c1, a2, b2, c2;
	if (a + b + c == 2) {
		if (a)
			printf("P");
		if (b)
			printf("R");
		if (c)
			printf("S");
		return;
	}
	if (a == b) {
		c1 = c2 = c / 2;
		a1 = a / 2;
		a2 = a - a1;
		b2 = b / 2;
		b1 = b - b2;
	} else if (a == c) {
		b1 = b2 = b / 2;
		a1 = a / 2;
		a2 = a - a1;
		c2 = c / 2;
		c1 = c - c2;
	} else if (c == b) {
		a1 = a2 = a / 2;
		b1 = b / 2;
		b2 = b - b1;
		c2 = c / 2;
		c1 = c - c2;
	}
	if (a1 < a2) {
		swap(a1, a2);
		swap(b1, b2);
		swap(c1, c2);
	} else if (a1 == a2) {
		if (b1 < b2) {
			swap(a1, a2);
			swap(b1, b2);
			swap(c1, c2);
		} else if (b1 == b2) {
			if (c1 < c2) {
				swap(a1, a2);
				swap(b1, b2);
				swap(c1, c2);
			}
		}
	}
	gao(a1, b1, c1);
	gao(a2, b2, c2);
}
int n, a, b, c, i, t, m, cnt;
int main() {
	setIO("A-large");
	int test;
	scanf("%d", &test);
	for (i = 1; i <= test; i++) {
		cnt = 0;
		scanf("%d%d%d%d", &n, &b, &a, &c);
		m = (1 << n);
		if ((m + 1) % 3 == 0)
			t = (m + 1) / 3;
		else
			t = (m - 1) / 3;
		if (a == t)
			cnt++;
		if (b == t)
			cnt++;
		if (c == t)
			cnt++;
		printf("Case #%d: ", i);
		if (cnt != 2)
			printf("IMPOSSIBLE");
		else
			gao(a, b, c);
		printf("\n");
	}
}
