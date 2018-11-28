#include <cstdio>
#include <algorithm>

using namespace std;

int vals[1004];
long long bef[1004];

int main(){
    int cases = 0;
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++){
        long long val = 0;
        long long E, R, N;
        scanf("%lld%lld%lld", &E, &R, &N);
        for (int j = 0; j < N; j++){
            scanf("%d", &vals[j]);
        }
        for (int j = 0; j < N; j++){
            int test = 1;
            while (j + test < N && vals[j] > vals[test+j]){
                test++;
            }
            if (j + test < N){
                bef[j] = test;
                //printf ("%d ", test);
            } else {
                bef[j] = -1;
                //printf ("-1 ");
            }
            //printf("\n");
        }
        long long e = E;
        for (int j = 0; j< N; j++){
            if (bef[j] == -1){
                val += vals[j]*e;
                e = 0;
            } else {
                val += vals[j]*(min(e, max(bef[j]*R+e-E, 0ll)));
                e -= min(e, max(bef[j]*R+e-E, 0ll));
            }
            e += R;
        }
        
        printf("Case #%d: %lld\n", i, val);
    }
}