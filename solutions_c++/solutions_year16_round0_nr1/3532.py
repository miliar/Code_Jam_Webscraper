#include <cstdio>
#include <cstring>

void determine(int v) {
    if (v == 0) {
        puts("INSOMNIA");
        return;
    }
    int used[10];
    int count = 0;
    memset(used, 0, sizeof used);
    for(int i = 1; ; i++) {
        long long r = i * 1ll * v;
        while (r > 0) {
            int dig = r % 10;
            if (!used[dig]) {
                count += 1;
                used[dig] = 1;
            }
            r /= 10;
        }
        if (count == 10) {
            printf("%lld\n", i * 1ll * v);
            return;
        }
    }
}

int main() {
    int testcount;
    scanf("%d", &testcount);
    for(int i = 1; i <= testcount; i++) {
        printf("Case #%d: ", i);
        int number;
        scanf("%d", &number);
        determine(number);
    }
}
