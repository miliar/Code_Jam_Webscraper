#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

int tt, n, k, id[20];
double p[20], sol;

void choose(int curr, int n, int choosen, int k) {
	if (choosen == k) {
		double P = 0.0;
		for (int i = 0; i < (1 << k); i++) {
			if (__builtin_popcount(i) != (k / 2)) continue;
			double currP = 1.0;
			for (int j = 0; j < k; j++) {
				if (i & (1 << j)) currP *= p[id[j]];
				else currP *= (1.0 - p[id[j]]);
			}
			P += currP;
		}
		sol = max(sol, P);
		return;
	}
	if (n - curr < k - choosen) return;
	id[choosen] = curr;
	choose(curr + 1, n, choosen + 1, k);
	choose(curr + 1, n, choosen, k);
}

int main() {
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
    	scanf("%d %d", &n, &k);
    	for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
    	sol = 0.0;
    	choose(0, n, 0, k);
    	printf("Case #%d: %.9lf\n", t, sol);
    }
    return 0;
}
