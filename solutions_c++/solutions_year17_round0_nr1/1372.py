#include <cstdio>
#include <cstring>

int main() {
    int t, k;
    char str[1010];
    scanf("%d", &t);
    
    for (int tcase = 1; tcase <= t; tcase++) {
        int res = 0;
        scanf("%s %d", str, &k);
        
        int n = strlen(str);
        bool possible = true;
        
        for (int i = 0; i < n; i++) {
            //printf("i -> %d, str == %s\n", i, str);
            if (i + k > n && str[i] == '-') {
                possible = false;
            } else if (str[i] == '-') {
                res++;
                for (int j = i; j < i + k; j++) {
                    str[j] = '+' + '-' - str[j];
                }
            }
        }
        
        if (possible) {
            printf("Case #%d: %d\n", tcase, res);        
        } else {
            printf("Case #%d: IMPOSSIBLE\n", tcase);        
        }
    }
    return 0;
}
