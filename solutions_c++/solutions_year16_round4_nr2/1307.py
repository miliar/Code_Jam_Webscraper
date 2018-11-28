#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 20
using namespace std;
double ans;
double sum;
int a[N];
int b[N];
double p[N];
int n, K;
void sear(int dep, int st) {
	if (dep == 1 + K / 2) {
		double temp = 1;
		for (int i = 1; i <= K; i++)
			if (b[i]) temp *= p[a[i]];
			else temp *= 1 - (p[a[i]]);
		sum += temp;
	}
	else
	for (int i = st; i <= K; i++) {
		b[i] = 1;
		sear(dep + 1, i + 1);
		b[i] = 0;
	}
}
void check() {
    sum = 0;
	memset(b, 0, sizeof b);
	sear(1, 1);
	ans = max(ans, sum);
}
void dfs(int dep, int st) {
	if (dep == K + 1) check();
	else {
		for (int i = st; i <= n; i++) {
			a[dep] = i;
			dfs(dep + 1, i + 1);
		}
	}
}
int cas, cases;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	scanf("%d", &cas);
	for (cases = 1; cases <= cas; cases ++) {
		scanf("%d%d", &n, &K);
		for (int i = 1; i <= n; i++)
			scanf("%lf", &p[i]);
		ans = sum = 0;
		dfs(1, 1);
		printf("Case #%d: %.6lf\n", cases, ans);
	}
}
