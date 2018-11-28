#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;

int T;
const int MAXT = 100;
const int MAXD = 1000;
const int MAXP = 1000;
int D;
int P[MAXD];

int minutes(int maxstack) {
    //int realms = 0;
    int min = 0;
    for (int d = 0; d < D; d++) {
        int m = (P[d] + maxstack - 1) / maxstack;
        min += m - 1;
        //realms = max(realms, (P[d] + m - 1) / m);
    }
    return min + maxstack; //realms;
}

int main() {
    scanf("%d",&T);
    for(int t = 1; t <= T; t++) {
        scanf("%d", &D);
        for(int d = 0; d < D; d++) {
            scanf("%d", &P[d]);
        }
        int bestms = 1e9;
        for(int b = 1; b <= MAXP; b++) {
            int mb = minutes(b);
            //fprintf(stderr, "%d takes %d\n", b, mb);
            if (mb < bestms) {
                bestms = mb;
            }
        }
        printf("Case #%d: %d\n", t, bestms);
    }
}
