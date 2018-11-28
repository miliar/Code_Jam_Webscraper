#include <cstdio>

int N;
long long P;
long long pow2[60];

bool chkBest(long long id) {
	if(id == pow2[N]) return false;
	int round = 1;
	long long sum = 0;
	long long A = pow2[N] - id - 1;
	while(A > 0) {
		sum += pow2[N - round];
		A = (A - 1) / 2;
		++round;
	}
	sum = pow2[N] - sum - 1;
	//printf("best %lld -> %lld\n", id, sum);
	return sum < P;
}

bool chkWorst(long long id) {
	if(id == pow2[N]) return false;
	int round = 1;
	long long sum = 0;
	long long A = id;
	while(A > 0) {
		sum += pow2[N - round];
		A = (A - 1) / 2;
		++round;
	}
	//printf("worst %lld -> %lld\n", id, sum);
	return sum < P;
}  


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	pow2[0] = 1;
	for(int i = 1; i < 60; ++i)
		pow2[i] = pow2[i - 1] * 2;
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		scanf("%d%lld", &N, &P);
		long long bg = 0, ed = pow2[N] - 1, mid;
		// find Worst Case
		while(true) {
			mid = (bg + ed) / 2;
			if(chkWorst(mid)) {
				if(!chkWorst(mid + 1)) break;
				else bg = mid + 1;
			} else ed = mid - 1;
		}
		long long worst = mid;
		bg = 0, ed = pow2[N] - 1;
		// find Worst Case
		while(true) {
			mid = (bg + ed) / 2;
			if(chkBest(mid)) {
				if(!chkBest(mid + 1)) break;
				else bg = mid + 1;
			} else ed = mid - 1;
		}
		long long best = mid;
		printf("Case #%d: %lld %lld\n", t, worst, best);
	}
}
