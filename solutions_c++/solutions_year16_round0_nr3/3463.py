#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <bitset>
using namespace std;

const int N = 32, M = 10007;

int s[N];
int cnt = 0;
int ans[N];
bool ok = false;
int n, m;

long long base_k(int k)
{
	long long res = 0;
	for(int i = n-1; i >= 0; --i) {
		res *= k;
		res += s[i];
	}
	return res;
}

int is_composite(long long k)
{
	int m = (int)(sqrt(k)+1);
	m = min(m, M);
	for(int i = 2; i <= m; ++i) {
		if(k % i == 0) {
			return i;
		}
	}
	return 0;
}

bool calc()
{
	for(int i = 2; i <= 10; ++i) {
		long long res = base_k(i);
		if((ans[i] = is_composite(res)) == 0) {
			return false;
		}
	}
	return true;
}

void dfs(int p)
{
	if(ok) {
		return;
	}
	if(p == n-1) {
		if(calc()) {
			if(++cnt == m) {
				ok = true;
			}
			for(int i = n-1; i >= 0; --i) {
				cout << s[i];
			}
			for(int i = 2; i <= 10; ++i) {
				cout << ' ' << ans[i];
			}
			cout << endl;
		}
		return;
	}
	s[p] = 0;
	dfs(p+1);
	s[p] = 1;
	dfs(p+1);
}

void work()
{
	cin >> n >> m;
	s[0] = s[n-1] = 1;
	dfs(1);
}

int main()
{
	#define LOCAL_
	#ifdef LOCAL
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);
	#endif

	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ":\n";
		work();
	}
	return 0;
}
