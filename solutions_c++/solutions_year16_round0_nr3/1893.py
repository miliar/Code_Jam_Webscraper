#include <cstdio>
#include <cstring>
#include "io.h"
using namespace std;


void toString(int n, char *str) {
    sprintf(str, "%d", n);
}

char str[100];
bool vis[1000];

int main() {
    setInput("a.in");
    setOutput("a.out");
    int T;
    int len;
    int n;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        memset(vis, false, sizeof(vis));
        scanf("%d", &n);
        int k = 1;
        int cnt = 0;
        int now = n;
        if (n == 0) goto next_case;
        while (true) {
            now = k*n;
            toString(now, str);
            len = strlen(str);
            for (int i = 0; i < len; i++) {
                if (!vis[str[i]]) {
                    cnt++;
                    vis[str[i]] = true;
                    if (cnt == 10) {
                        goto next_case;
                    }
                }
            }
            k++;
        }
        next_case:
            if (n == 0) {
                printf("Case #%d: INSOMNIA\n", t);
            } else {
                printf("Case #%d: %d\n", t, k*n);
            }
    }

    return 0;
}