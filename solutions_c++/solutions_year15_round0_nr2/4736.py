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

const int maxn = 1111;
int p[maxn];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int C = 1; C <= Cases; ++C){
		printf("Case #%d: ", C);
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d", &p[i]);
		int ans = 1000;
		for (int i = 1; i <= 1000; ++i){
			int tmp = i;
			for (int j = 1; j <= n; ++j){
				tmp += (p[j] - 1) / i;
			}
			ans = min(ans, tmp);
		}
		printf("%d\n", ans);
	}
	return 0;
}

