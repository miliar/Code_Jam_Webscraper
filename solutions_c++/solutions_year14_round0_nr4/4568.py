#include<iostream>
#include<vector>
#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<string.h>
#include<string>
#include<cassert>
#include<stack>
#include<queue>
#include<cmath>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int, int> PI;

int main() {
    double A[1000];
    double B[1000];
    bool usedB[1000];
    int optimalWar;
    int deceitfulWar;
    int t;
    int N;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        memset(usedB, false, sizeof(usedB));
        optimalWar = 0;
        deceitfulWar = 0;
        scanf("%d", &N);
        
        for(int i = 0; i < N; i++) {
            scanf("%lf", &A[i]);
        }
        for(int i = 0; i < N; i++) {
            scanf("%lf", &B[i]);
        }
        
        sort(A, A + N);
        sort(B, B + N);

        // for(int i = 0; i < N; i++) {
        //     printf("%lf ", A[i]);
        // }
        // printf("\n");
        // for(int i = 0; i < N; i++) {
        //     printf("%lf ", B[i]);
        // }
        // printf("\n");

        for(int i = 0; i < N; i++) {
            int minIdx = N - 1;
            int j;
            for(j = 0; j < N; j++) {
                if(usedB[j]) continue;
                minIdx = min(minIdx, j);
                if(A[i] < B[j]) {
                    usedB[j] = true;
                    break;
                }
            }
            if(j == N) {
                // no value in B is greater than A[i]
                optimalWar++;
                usedB[minIdx] = true; // use minIdx
            }
        }

        int jSt = 0; int jEnd = N - 1;

        for(int i = 0; i < N; i++) {
            if(A[i] > B[jSt]) {
                // use A[i] to conquer the block B[jSt]  because that's the smallest actual block naomi could use to conquer B[jSt].
                jSt++;
                deceitfulWar++;
            }
            else {
                jEnd--;
            }
        }
        assert(jEnd - jSt == -1);

        printf("Case #%d: %d %d\n", tt, deceitfulWar, optimalWar);
    }
}