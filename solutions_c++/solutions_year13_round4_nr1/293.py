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

const int MAX_N = 10000 + 10;
const int MOD = 1000002013;

int N, M;
LL a[MAX_N];
int st[MAX_N], ed[MAX_N], num[MAX_N];
int cx[MAX_N], tot;

LL w(LL len)
{
	return (len * (N + N - len + 1) / 2) % MOD;
}

LL getCost(LL cost)
{
	LL cc = 0;
	for(int i = 0; i < M; ++ i) {
		cc = (cc + w(ed[i] - st[i]) * num[i] % MOD) % MOD;
	}
	cc -= cost;
	cc = (cc % MOD + MOD) % MOD;
	return cc;
}

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> N >> M;
	tot = 0;
	
	for(int i = 0; i < M; ++ i) {
		cin >> st[i] >> ed[i] >> num[i];
		cx[tot ++] = st[i];
		cx[tot ++] = ed[i];
	}
	
	sort(cx, cx + tot);
	int ctot = 0;
	for(int i = 0; i < tot; ++ i) {
		if (i == 0 || cx[i] != cx[i - 1])
			cx[ctot ++] = cx[i];
	}
	tot = ctot;
	
	memset(a, 0, sizeof a);
	
	for(int i = 0; i < M; ++ i) {
		for(int j = 0; j < tot - 1; ++ j) {
			if (st[i] <= cx[j] && cx[j + 1] <= ed[i])
				a[j] = a[j] + num[i];
		}
	}
	
	int flag;
	LL cost = 0;
	for( ; ; ) {
		flag = true;
		for(int j = 0; j < tot - 1; ) {
			if (! a[j]) {
				++ j;
				continue;
			}
			flag = false;
			int k = j;
			LL mind = a[k];
			for( ; a[k] && k < tot - 1; ++ k) {
				mind = min(mind, a[k]);
			}
			
			k = j;
			for( ; a[k] && k < tot - 1; ++ k) {
				a[k] -= mind;
			}
			
			mind %= MOD;
			cost = (cost + (mind * w(cx[k] - cx[j])) % MOD) % MOD;
			j = k;
		}
		if (flag) break;
	}
	cout << getCost(cost) << endl;
}

int main()
{
	//freopen("A.in", "r", stdin); freopen("A.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out2", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int testcase; scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) solve(i);
	fclose(stdout);
	return 0;
}
