#include<stdio.h>
#include<set>
using namespace std;

int T, TT;
int R, N, M, K;
int A[16];
set<int> S[64];

inline void build(int a, int b, int c, int i) {
        S[i].insert(1);
        S[i].insert(a);
        S[i].insert(b);
        S[i].insert(c);
        S[i].insert(a*b);
        S[i].insert(b*c);
        S[i].insert(c*a);
        S[i].insert(a*b*c);
}

inline bool match(int id) {
        for(int i = 0; i < K; ++i)
                if(S[id].find(A[i]) == S[id].end()) return false;
        return true;
}

int main() {
        for(int i = 2; i <= 5; ++i)
                for(int j = 2; j <= 5; ++j)
                        for(int k = 2; k <= 5; ++k)
                                build(i, j, k, (i-2)*16+(j-2)*4+(k-2));
	scanf("%d\n", &TT);
	for(int T = 1; T <= TT; ++T) {
		scanf("%d %d %d %d", &R, &N, &M, &K);
		printf("Case #%d:\n", T);
                for(int rr = 0; rr < R; ++rr) {
                        for(int i = 0; i < K; ++i)
                                scanf("%d", &A[i]);
                        int id = 0;
                        for(; id < 64; ++id)
                                if(match(id)) break;
                        printf("%d%d%d\n", id/16+2, ((id/4)&0x3)+2, (id&0x3)+2);
                }
	}
}



