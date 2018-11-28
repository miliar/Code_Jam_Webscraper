#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int T, N;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T0 = 0;
    scanf("%d", &T);
    for ( ; T; --T) {
        scanf("%d", &N);
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", ++T0);
            continue;
        }
        bool used[10];
        memset(used, 0, sizeof(used));
        int cnt = 0, cnta = 0;
        for (int i = N; ; i += N) {
            for (int j = i; j; j /= 10)
                if (!used[j % 10]) {
                    used[j % 10] = true;
                    ++cnt;
                }
            if (cnt == 10) {
                printf("Case #%d: %d\n", ++T0, i);
                break;
            }
            ++cnta;
            if (cnta == 100)
                break;
        }
        if (cnta == 100) {
            printf("Case #%d: INSOMNIA\n", ++T0);
        }
    }
    return 0;
}
