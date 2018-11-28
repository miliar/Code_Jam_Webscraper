#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int MAX_N = 100 + 10;

LL ret;
int pret[MAX_N];
int N;
int p[MAX_N], used[MAX_N];
LL x[MAX_N], y[MAX_N];

LL xx(int s, int u, int v)
{
	return 1LL * (x[u] - x[s]) * (y[v] - y[s]) - 1LL * (x[v] - x[s]) * (y[u] - y[s]);
}

int sign(LL x)
{
	if (x < 0) return -1;
	if (x) return 1;
	return 0;
}

int cross(int u0, int u1, int v0, int v1)
{
	if (sign(xx(u0, u1, v0)) * sign(xx(u0, u1, v1)) < 0 
		&& sign(xx(v0, v1, u0)) * sign(xx(v0, v1, u1)) < 0)
		return true;
	return false;
}

int check()
{
	LL sum = 0;
	for(int i = 0; i < N; ++ i) {
		sum += xx(N, p[i], p[(i + 1) % N]);
	}
	
	sum = abs(sum);
	if (sum > ret) {
		ret = sum;
		for(int i = 0; i < N; ++ i) 
			pret[i] = p[i];
	}
	
	return false;
}

int on(int s, int u, int v)
{
	if (sign(xx(s, u, v))) return false;
	if (x[u] == x[v]) {
		if (y[s] <= min(y[u], y[v])) return false;
		if (y[s] >= max(y[u], y[v])) return false;
		return true;
	}
	if (x[s] <= min(x[u], x[v])) return false;
	if (x[s] >= max(x[u], x[v])) return false;
	return true;
}

int OK(int u, int v, int cur)
{
	for(int j = 0; j < cur; ++ j)
		if (cross(p[j], p[j + 1], p[u], p[v])) {
			return false;
		}
	for(int j = 0; j < N; ++ j) {
		if (j == p[u] || j == p[v]) continue;
		if (on(j, p[u], p[v]))
			return false;
	}
	return true;
}

int dfs(int cur)
{
	if (cur == N) {
		if (! OK(0, N - 1, N - 1)) return false;
		if (check()) return false;
		return false;		
	}
	
	for(int i = 0; i < N; ++ i) {
		if (used[i]) continue;
		p[cur] = i;
		if (! OK(cur - 1, cur, cur))
			continue;
		used[i] = true;
		if (dfs(cur + 1)) return true;
		used[i] = false;
	}
	
	return false;
}

void solve(int test)
{
	printf("Case #%d:", test);
	cin >> N;
	memset(x, 0, sizeof x);
	memset(y, 0, sizeof y);
	for(int i = 0; i < N; ++ i) {
		cin >> x[i] >> y[i];
	}
	
	ret = 0;
	memset(used, 0, sizeof used);
	p[0] = 0; used[0] = true;
	dfs(1);
	//cout << ret << endl;
	for(int i = 0; i < N; ++ i)
		printf(" %d", pret[i]);
	printf("\n");
}

int main()
{
	//freopen("B.in", "r", stdin); freopen("B.out", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	//freopen("B-large.in", "r", stdin); freopen("E-large.out", "w", stdout);
	int testcase; scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) solve(i);
	fclose(stdout);
	return 0;
}
