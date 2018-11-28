#include<cstdio>
#include<algorithm>
using namespace std;

#define MAXN 1010

int used[100010];

int naomi[MAXN], ken[MAXN];
double naomif[MAXN], kenf[MAXN];
bool usedNaomi[MAXN], usedKen[MAXN];
int T, N;

// int findn(int num)
// {
//     if ( num < 10 )
//         return 1;
//     if ( num < 100 )
//         return 2;
//     if ( num < 1000 )
//         return 3;
//     if ( num < 10000 )
//         return 4;

//     return 5;

//     //continue until max int
// }

int main() {
    scanf("%d",&T);
    for (int t=1; t<=T; ++t) {
        memset(usedNaomi, false, sizeof usedNaomi);
        memset(usedKen, false, sizeof usedNaomi);
        scanf("%d",&N);
        int waste;
        for (int i=0; i<N; i++) {
            scanf("%lf",  &naomif[i]);
            naomi[i] = naomif[i]*100000;
        }
        for (int i=0; i<N; i++) {
            scanf("%lf", &kenf[i]);
            ken[i] = kenf[i]*100000;
        }
        sort(naomi, naomi+N);
        sort(ken, ken+N);
        for (int i=0; i<N; i++) {
            used[ken[i]] = 1;
        }

        // calc war score
        int km=0, kM = N-1;
        int warScore = 0, dwarScore = 0;
        for (int i=N-1; i>=0; i--) {
            if (naomi[i]>  ken[kM] ) {
                km++;
                warScore++;
            } else {
                kM--;
            }
        }

        // deceitful war
        for (int i=0; i<N; i++) { // ken's possible plays
            // printf("HOLA\n");
            if (usedKen[i]) continue;
            for (int j=0; j<N; j++) { // naomi's possible plays
                if (usedNaomi[j]) continue; // already used this one
                if (naomi[j] < ken[i])  continue; // won't win
                // look for weight that would make ken play `i` card.
                int pos=-1;
                int kenHigh = -1;
                int kenHighPos;
                for (kenHighPos=N-1; kenHighPos>=0&&(kenHigh==-1); kenHighPos--) {
                    if (!usedKen[kenHighPos]) kenHigh = ken[kenHighPos];
                }
                kenHighPos++;
                // printf("KenHigh = %d\n", kenHigh);
                for (int k=kenHigh; k<100000&&(pos==-1); ++k) {
                    if (!used[k]) pos = k;
                }

                if (pos != -1) {
                    // printf("Saying %d\n", pos);
                    used[pos] = 2;
                    dwarScore++;
                    usedNaomi[j] = true;
                    usedKen[i] = true;
                } else {
                    // i--;
                    // printf("Trying to make you play your highest...\n");
                    int usingPos = -1;
                    // printf("kenHighPos = %d\n", kenHighPos);
                    for (int k=kenHigh-1; k>=0&&(usingPos==-1); k--) {
                        if (!used[k]) {
                            usingPos = k;
                        } else if (used[k] == 1) {
                            kenHighPos = k;
                        }
                    }
                    // printf("Saying... %d\n", usingPos);
                    // printf("kenHighPos = %d\n", kenHighPos);
                    used[usingPos] = 2;
                    usedNaomi[j] = true;
                    usedKen[kenHighPos] = true;
                    i--;
                }
                break;
            }
            // bool played = false;
            // for (int j=0; j<N&&!played; j++) {
            //     if (usedNaomi[j]) continue;
            //     if (naomi[j] < ken[i]) continue;
            //     int pos;
            //     bool found = false;
            //     for (int k=ken[kM+1]; k<100000&&!found; ++k)
            //         if (!used[k]) found = true, pos = k;
            //     if (found) {
            //         printf("Saying %d\n", pos);
            //         used[pos] = true;
            //         dwarScore++;
            //         played = true;
            //         usedNaomi[j] = true;
            //     } else {
            //         printf("No puedo ganarle at all\n");
            //         played = true;
            //         for (int k=0; k<N; k++)
            //             if (!usedNaomi[i]) {
            //                 usedNaomi[k] = true;
            //                 break;
            //             }
            //     }
            // }
        }
        // for (int i=N-1; i>=0; i--){
        //     if (naomi[i] > ken[kM]) {
        //         printf("Saying legal %d\n", naomi[i]);
        //         km++;
        //         dwarScore++;
        //         used[naomi[i]] = true;
        //     } else if (naomi[i] > ken[km]) {
        //         // try to find something to beat this
        //         bool found = false;
        //         int pos;
        //         for (int k=ken[kM]+1; k<100000&&!found; ++k) {
        //             if (!used[k]) found = true, pos=k;
        //         }
        //         if (found) {
        //             printf("Saying %d\n", pos);
        //             km++;
        //             used[pos] = true;
        //             dwarScore++;
        //         } else {
        //             printf("No puedo ganarle at all.\n");
        //             kM--;
        //         }
        //     } else {
        //         printf("No puedo ganarle at all.\n");
        //         km++;
        //         used[naomi[i]] = true;
        //     }
        // }
        printf("Case #%d: %d %d\n", t, dwarScore, warScore);
    }
    return 0;
}
