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

const int maxn = 100000;
int c[maxn];

int main(){
	freopen("A0.in", "r", stdin);
	freopen("A0.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int C = 1; C <= Cases; ++C){
		printf("Case #%d: ", C);
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%d", &c[i]);
		sort(c, c + n);
		int l = 0, r = n - 1, ans = 0;
		while (l <= r){
			if (l == r){
				++ans;
				break;
			}
			if (c[l] + c[r] <= m){
				++l;
				--r;
				++ans;
			} else {
				--r;
				++ans;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}

