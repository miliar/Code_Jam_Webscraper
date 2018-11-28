#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <bitset>
using namespace std;
bitset<10> b;

int check_for_sleep(int x) {
    char s[10];
    sprintf(s, "%d", x);
    for (int i = 0; s[i]; i++) 
        b[s[i] - '0'] = 1;
    int done = 0;
    for (int i = 0; i < 10; i++)
        if (b[i]) done++;
    return (done == 10);
}

int main() {
    int t, n;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        if (!n) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        int limit = 100;
        b.reset();
        for (int j = 1; j <= limit; j++) {
            int x = j * n;
            if (check_for_sleep(x)) {
                printf("Case #%d: %d\n", i, x);
                break;
            }
        }
    }
    return 0;
}
