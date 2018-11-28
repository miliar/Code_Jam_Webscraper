#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <cmath>
#include <cstdlib>
#include <map>
#include <climits>
#include <limits>
#include <functional>
#include <bitset>
using namespace std;
#define LL long long
#define LD long double
#define mod 1000000007
int tc, tcn, N, J, p[1 << 16],ans[11];
LL cur[11];
vector<int> v[17];
map <int, int> mp;

void getPrime() {
	for (int i = 2; i < (1 << 16); i++) {
		if (!p[i]) {
			if (i >= 10000)
				continue;
			for (int j = i*i; j < (1 << 16); j += i)
				p[j] = 1;
		}
	}
}

bool isPrime(LL cur, int b) {
	int ret = 1;
	v[b].clear();
	if (cur % 2 == 0) {
		ret = 0;
		v[b].push_back(2);
	}
	
	for (LL i = 3; i*i <= cur && i <= 10000; i += 2) {
		if (!p[i] && cur%i == 0) {
			ret = 0;
			v[b].push_back(i);
			if (v[b].size() >= 1)
				return ret;
		}
	}
	return ret;
}

bool isPos(int idx) {
	return true;
	if (idx == 10)
		return true;
	for (int i = 0; i < v[idx].size(); i++) {
		if (!mp.count(v[idx][i])) {
			mp[v[idx][i]] = 1;
			ans[idx] = v[idx][i];
			if (isPos(idx + 1))
				return true;
		}
	}



	return false;
}

void init() {
	
	//

	
}

void solve() {
	getPrime();
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", ++tcn);
		int n = N;
		if (n > 16)
			n /= 2;
		int cnt = 0;
		for (int i = (1 << (n-1)) + 1; i < (1 << n); i += 2) {
			int fail = 0;
			for (int j = 2; j <= 10; j++) {
				cur[j] = 0;
				LL t = 1;
				for (int k = 1; k <= i; k<<=1, t *= (LL)j) {
					if (k&i)
						cur[j] += t;
				}
				
				if (isPrime(cur[j],j)) {
					fail = 1;
					break;
				}
			}
			if (fail) continue;
			mp.clear();
			if (isPos(2)) {
				cnt++;

				for (int k = (1<<(n-1)); k >=1; k>>=1) {
					printf("%d", (k&i) ? 1 : 0);
				}
				if (n != N) {
					for (int k = (1 << (n - 1)); k >= 1; k >>= 1) {
						printf("%d", (k&i) ? 1 : 0);
					}
				}
				for (int j = 2; j <= 10; j++) {
					printf(" %d", v[j][0]);
				}
				puts("");
				if (cnt == J)
					break;
			}
		}
	}
}

int main(void) {
	//freopen("CL.in", "r", stdin);
	//freopen("CLout.txt", "w", stdout);
	solve();
	return 0;
}