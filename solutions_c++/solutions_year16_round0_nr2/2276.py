#include <cstdio>
#include <cstring>
char a[1111];
int main() {
    int t;
    scanf("%d",&t);
    for (int tc=1; tc<=t; tc++) {
        scanf("%s",a);
        int n = strlen(a);
        printf("Case #%d: ",tc);
        int ans = 0;
        bool first = true;
        for (int i=0; i<n; i++) {
            if (a[i] == '-') {
                if (i+1 < n) {
                    if (a[i+1] == '+') {
                        if (first) {
                            ans += 1;
                            first = false;
                        } else {
                            ans += 2;
                        }
                    }
                } else {
                    if (first) {
                        ans += 1;
                        first = false;
                    } else {
                        ans += 2;
                    }
                }
            } else {
                first = false;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}

