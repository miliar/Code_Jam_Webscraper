#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<unordered_set>
#include<string>
using namespace std;

#define BASE 1000000007

int nCase;
long long ANS[8][8];
char M[8][8];
int R, C;

unordered_set<string> SEEN;

bool good(int r, int c) {
    int s = 0;
    int lf = (c==0) ? (C-1) : (c-1);
    int rt = (c==C-1) ? 0 : (c+1);
    if(M[r][lf] == M[r][c]) s++;
    if(M[r][rt] == M[r][c]) s++;
    if(r > 0 && M[r-1][c]==M[r][c]) s++;
    if(r < R-1 && M[r+1][c]==M[r][c]) s++;
    return s == M[r][c];
}

bool isnew() {
    char S[64] = {0}, Z[64] = {0};
    string s;
    for(int t = 0; t < C; ++t) {
        for(int r = 0; r < R; ++r)
            for(int c = 0; c < C; ++c) S[r*C+c] = M[r][(c+t)%C];
        if(Z[0] == 0 || strcmp(S, Z)<0) strcpy(Z, S);
    }
    s = string(Z);
    if(SEEN.find(s) != SEEN.end()) return 0;
    SEEN.insert(s);
/*    for(int r = 0; r < R; ++r) {
        for(int c = 0; c < C; ++c) fprintf(stderr, "%d", M[r][c]);
        fprintf(stderr, "\n");
    }
    fprintf(stderr, "\n");*/
    return 1;
}

long long calc(int r, int c) {
    if(c == C) return calc(r+1, 0);
    if(r == R) {
        for(int c = 0; c < C; ++c)
            if(!good(r-1,c)) return 0;
        return isnew() ? 1 : 0;
    }
    long long s = 0;
    for(int x = 1; x <= 4; ++x) {
        M[r][c] = x;
        if(r > 0 && !good(r-1,c)) continue;
        s += calc(r, c+1);
    }
    return s;
}

int main() {
    for(int r = 2; r <= 6; ++r) for(int c = 3; c <= 6; ++c) {
        R = r, C = c;
        SEEN.clear();
//        fprintf(stderr, "========== %d %d\n", R, C);
        ANS[r][c] = calc(0, 0);
//        printf("%d %d %lld\n", R, C, ANS[r][c]);
    }
	scanf("%d", &nCase);
	for(int casei = 1; casei <= nCase; ++casei) {
		scanf("%d %d", &R, &C);
		printf("Case #%d: %lld\n", casei, ANS[R][C]);
	}
}

