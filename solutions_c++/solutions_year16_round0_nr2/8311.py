#include <cstdio>
#include <cstring>

int main(void) {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-out.txt", "w", stdout);
    
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        
        char s[105]; scanf("%s", s);
        int len = strlen(s);
        bool a[105];
        for (int i = 0; i < len; i++) {
            if (s[i] == '+') a[i] = true;
            else a[i] = false;
        }
        
        int ans = 0;
        for (int i = len-1; i >= 0; i--) {
            while (i >= 0 && a[i]) i--;
            if (i >= 0) ans++;
            for (int j = i; j >= 0; j--) a[j] = !a[j];
        }
        printf("%d\n", ans);
    }
    return 0;
}