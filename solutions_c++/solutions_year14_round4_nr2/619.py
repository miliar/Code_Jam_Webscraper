#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

const int maxn = 10000;
int c[maxn];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int C = 1; C <= Cases; ++C){
		printf("Case #%d: ", C);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &c[i]);
		int ans = 0;
		for (; n > 0;){
			int k = 0;
			for (int i = 0; i < n; ++i)
				if (c[i] < c[k]) k = i;
			ans += min(k, n - 1 - k);
			for (int i = k; i < n - 1; ++i){
				c[i] = c[i + 1];
			}
			--n;
		}
		printf("%d\n", ans);
	}
	return 0;
}

