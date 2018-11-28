#include<stdio.h>
#include<algorithm>
using namespace std;

#define BASE 1000002013LL

typedef struct Node {
	long long pos, val;
	bool operator<(const struct Node &a) const {
		return pos < a.pos;
	}
}Node;

int T, TT;
int N, M;
Node IN[1024], OUT[1024];
long long A1, A2;

inline long long getDist(long long d) {
	return (N+(N-d+1))*d/2;
}

int main() {
	scanf("%d\n", &TT);
	for(int T = 1; T <= TT; ++T) {
		scanf("%d %d", &N, &M);
		A1 = A2 = 0;
		for(int i = 0; i < M; ++i) {
			scanf("%lld %lld %lld", &IN[i].pos, &OUT[i].pos, &IN[i].val);
			OUT[i].val = IN[i].val;
			A1 += IN[i].val * getDist(OUT[i].pos-IN[i].pos);
			A1 %= BASE;
		}
		sort(IN, IN+M);
		sort(OUT, OUT+M);
		for(int i = M-1; i >= 0; --i) {
			for(int j = 0; j < M && IN[i].val > 0; ++j)
				if(OUT[j].pos >= IN[i].pos) {
					long long v = min(IN[i].val, OUT[j].val);
					IN[i].val -= v;
					OUT[j].val -= v;
					A2 += v * getDist(OUT[j].pos-IN[i].pos);
					A2 %= BASE;
				}
		}
		long long ans = A1 - A2;
		if(ans < 0) ans += BASE;
		printf("Case #%d: %lld\n", T, ans);
	}
}
