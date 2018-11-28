#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;
int T;
int N;
double V,X;
double C[1000], R[1000];

void solve(int num) {
	scanf("%d%lf%lf", &N, &V, &X);
	REP(n,N) {
		scanf("%lf%lf", &R[n], &C[n]);
	}
	double maxi = C[0], mini = C[0];
	REP(n,N) {
		maxi = max(maxi,C[n]);
		mini = min(mini,C[n]);
	}
	if (X > maxi || X < mini) {
		printf("Case #%d: IMPOSSIBLE\n", num);
		return;
	}
	double time;
	if (N == 1) {
		time = V / R[0];
	}
	if (N == 2) {
		if (C[0] == C[1])
			time = V / (R[0] + R[1]);
		else if (C[0] == X) {
			time = V / R[0];
		}
		else if (C[1] == X) {
			time = V / R[1];
		}
		else {
			double x = R[0] * (X - C[0]) / R[1] / (C[1] - X);
			double t0 = V / (R[0] + x*R[1]);
			double t1 = x*t0;
			time = max(t0,t1);
		}
	}

	printf("Case #%d: %lf\n", num, time);
	return;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		solve(t+1);
	}
	return 0;
}
