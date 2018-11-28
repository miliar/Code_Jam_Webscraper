#include <cstdio>
#include <algorithm>

#define Nmax 10001

using namespace std;

int T, N, S, v[Nmax];
bool added[Nmax];

int main(){

    freopen("fis.in", "r", stdin);
    freopen("fis.out", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; ++t){
    
        int sol = 0;
    
        scanf("%d%d", &N, &S);

        for (int i = 1; i <= N; ++i){

            scanf("%d", &v[i]);
            added[i] = 0;
        }

        sort(v + 1, v + N + 1);

        int p  = 0;
        int u = N;

        int nrAdded = 0;
        while (nrAdded < N){
            nrAdded++;
            sol++;
            ++p;
            added[p] = 1;

            for (int j = N; j > p; --j){

                if (!added[j] && v[j] + v[p] <= S){
                    nrAdded++;
                    added[j] = 1;
                    break;
                }
            }

        }
        printf("Case #%d: %d\n", t, sol);
    }

    return 0;
}