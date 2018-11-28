#include <cstdio>
#include <iostream>

using namespace std;

int T, N, ans;
bool was[10];

void mark(int x) {
    do {
        was[x % 10] = true;
        x /= 10;
    } while (x > 0);    
}

int count() {
    int res = 0;
    for (int i = 0; i < 10; i++) {
        res += was[i];
    }
    return res;
}

int main() {
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        scanf("%d", &N);
        for (int i = 0; i < 10; i++) {
            was[i] = false;
        }
        printf("Case #%d: ", test + 1);
        if (N == 0) {
            printf("INSOMNIA");
        }
        else {
            ans = N;
            mark(ans);
            while (count() < 10) {
                ans += N;
                mark(ans);
            }
            printf("%d", ans);
        }
        printf("\n");
    }
    return 0;
}
