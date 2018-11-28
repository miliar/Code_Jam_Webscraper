#include <bits/stdc++.h>

int n;
char s[1001];

int solve() {
    int res = 0;
    int sum = s[0] - '0';
    
    for (int i = 1; i <= n; i++) {
        int t = s[i] - '0';
        while (sum < i) {
            sum++;
            res++;
        }
        sum += t;
    }
    
    return res;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        scanf("%d", &n);
        for (int i = 0; i <= n; i++) {
            scanf(" %c", &s[i]);
        }
        s[n + 1] = 0;
        
        //printf("%s\n", s);
        
        printf("Case #%d: ", test);
        printf("%d", solve());
        printf("\n");
    }

    return 0;
}
