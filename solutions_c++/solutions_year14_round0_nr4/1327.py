#include <cstdio>
#include <algorithm>
using namespace std;

#define MaxN 1010

int main() {
    int T;
    scanf("%d\n", &T);    
    for (int x = 0; x < T; x++) {
        
        int deceit, war, N;
        double a[MaxN], b[MaxN];
        
        scanf("%d\n", &N);
        for (int i = 0; i < N; i++)
            scanf("%lf", &a[i]);
        for (int i = 0; i < N; i++)
            scanf("%lf", &b[i]);
        sort(a, a + N);
        sort(b, b + N);
        
        /*
        for (int i = 0; i < N; i++)
            printf("%lf ", a[i]);
        printf("\n");
        for (int i = 0; i < N; i++)
            printf("%lf ", b[i]);
        printf("\n");
        */
        
        int i = 0, j = 0;
        deceit = 0;
        while (i < N) 
            if (a[i] < b[j]) i++;
            else {
                deceit++;
                j++; i++;
            }
            
        war = 0;
        bool used[MaxN] = {0};
        for (int i = N-1; i >= 0; i--) {
            int j = 0, pr = 0;
            while ((a[i]>b[j] || used[j]) && j < N ) j++;
            if (j == N) {
                while (used[pr]) pr++;
                used[pr] = true;
                war++;
            }else {
                used[j] = true;
            }
        }
    
    
        printf("Case #%d: %d %d\n", x+1, deceit, war);
    }
    return 0;
}
