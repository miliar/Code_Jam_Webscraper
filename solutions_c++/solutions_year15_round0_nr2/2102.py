#include <cstdio>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

int T;
int D;
int P[1000];

int solve() {
    sort(P, P + D, greater<int>());

    int result = P[0];
    for(int mini = 1; mini <= P[0]; mini++) {
        int additional = 0;
        for(int i = 0; i < D; i++) {
            additional += P[i] / mini;
            if(P[i] % mini == 0) additional--;
        }
        result = min(result, additional + mini);
    }

    return result;
}

int main() {
    scanf("%d", &T);
    for(int c = 1; c <= T; c++) {
        scanf("%d", &D);
        for(int i = 0; i < D; i++) { scanf("%d", P + i); }
        int result = solve();
        printf("Case #%d: %d\n", c, result);
    }
    return 0;
}


