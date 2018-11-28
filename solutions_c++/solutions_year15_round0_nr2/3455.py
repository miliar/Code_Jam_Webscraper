#include <cstdio>
#include <cassert>
#define MAX_N 1010
#define INF 1000000

int max(int a, int b) { return (a>b)?a:b; }
int min(int a, int b) { return (a<b)?a:b; }

int array_max(int *arr, int n) {
    int res = arr[0];
    for(int i=1; i<n; i++) {
        res = max(arr[i], res);
    }
    return res;
}

int metric(int level, int *arr, int n) {
    int cnt = 0;
    for(int i=0;i<n;i++) {
        cnt += arr[i] / level;
        if(arr[i] % level == 0) cnt--;
    }
    return cnt;
}

int solve(int n, int *plates) {
    int greatest = array_max(plates, n);
    int best = INF;
    
    for(int level = 1; level <= greatest; level++) {
        best = min(best, level + metric(level, plates, n));
        //printf("Solution for level %d: %d + %d = %d\n", level, level, metric(level, plates, n), level + metric(level, plates, n));
    }

    return best;
}

int main() {
    int n, plates[MAX_N], T;

    scanf("%d", &T);

    for(int t=1; t<=T; t++) {
        scanf("%d", &n);
        for(int i=0; i<n; i++) {
            scanf("%d", &plates[i]);
        }

        printf("Case #%d: %d\n", t, solve(n, plates));
    }

    return 0;
}
