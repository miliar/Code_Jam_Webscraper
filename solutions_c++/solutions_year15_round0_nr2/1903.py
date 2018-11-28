#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAXN 1005
using namespace std;

int p[MAXN];

int main(){
	int n, t;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <=t; tt++){
	scanf("%d", &n);
	int mx = 0;
	for (int i = 0; i<n; i++) {
		scanf("%d", &p[i]);
		mx = max(mx, p[i]);
	}
	int sum, mn = mx, tmp;
	for (int k = 1; k <= mx; k++){
		sum = 0;
		for (int i = 0; i<n; i++){
			if (p[i] > k) {
				tmp = ((p[i] - k) %k)>0;
				sum += (p[i] - k) /k + tmp;
			}
		}
		mn = min(mn, sum + k);
	}
	printf("Case #%d: %d\n", tt, mn);
	}
	return 0;
}
