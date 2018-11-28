#include <cstdio>
#include <cassert>
#include <memory.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        char buf[105];
        scanf("%s", buf);
        int n = strlen(buf);
        buf[n] = '+';
        int ans = 0;
        for (int i = 0; i < n; i++)
            ans += buf[i] != buf[i + 1];
        printf("Case #%d: %d\n", i + 1, ans);
    }
}
