#include<stdio.h>
#include<algorithm>
using namespace std;

struct Node {
	int v, i;
	bool operator<(const struct Node &a) const {
		if(v != a.v) return v > a.v;
		else return i < a.i;
	}
};

int T, TT;
int E, R, N;
Node V[16384];
int J[16384], C[16384];

inline int min(int a, int b) { return a < b ? a : b; }

inline int request(int i, int c) {
        if(i == 0 || J[i] >= c) {
                int t = min(J[i], c);
                J[i] -= t;
                C[i+1] -= t;
                return t;
        }
        int t = min(J[i], c);
        J[i] -= t;
        if(c > t && i > 0 && C[i] > 0) t += request(i-1, min(C[i], c-t));
        C[i+1] -= t;
        return t;
}

int main() {
	scanf("%d\n", &TT);
	for(int T = 1; T <= TT; ++T) {
		scanf("%d %d %d", &E, &R, &N);
		for(int i = 0; i < N; ++i) {
			scanf("%d", &V[i].v);
			V[i].i = i;
			J[i] = R, C[i] = E - R;
		}
                J[0] = E;
		sort(V, V+N);
		long long ans = 0;
		for(int i = 0; i < N; ++i) {
			int e = J[V[i].i];
                        if(V[i].i > 0) e += request(V[i].i-1, C[V[i].i]);
			ans += V[i].v * (long long)e;
			J[V[i].i] = 0;
			/*fprintf(stderr, "(%d,%d)\t%lld\t", V[i].i, V[i].v, ans);
			for(int j = 0; j < N; ++j) fprintf(stderr, "%d ", J[j]);
			fprintf(stderr, "\n");*/
		}

		printf("Case #%d: %lld\n", T, ans);
	}
}

