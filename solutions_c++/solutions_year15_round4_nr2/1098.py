#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define eps (1e-5)

typedef long double ld;
typedef pair<ld, ld> pdd;

int TC, N;
ld X, C[110], R[110], V;
ld minc, maxc;

int main() {
    scanf("%d", &TC);
    rep(tc, TC) {
	minc = 100.0; maxc = 0.0;
	printf("Case #%d: ", tc + 1);
	scanf("%d %Lf %Lf", &N, &V, &X);

	rep(i, N) {
	    scanf("%Lf %Lf", &R[i], &C[i]);
	    minc = min(minc, C[i]);
	    maxc = max(maxc, C[i]);
	}

	if(X < minc - eps || X > maxc + eps) {
	    puts("IMPOSSIBLE");
	    continue;
	}

	if(N == 1) printf("%.8Lf\n", V / R[0]);
	else {
	    ld al = V * X;
	    if(C[0] == C[1]) {
		printf("%.8Lf\n", V / (R[0] + R[1]));
	    } else {
		ld x = (al - C[1] * V) / (C[0] - C[1]);
		printf("%.8Lf\n", max(x / R[0], (V - x) / R[1]));
	    }
	}
    }
    return 0;
}
