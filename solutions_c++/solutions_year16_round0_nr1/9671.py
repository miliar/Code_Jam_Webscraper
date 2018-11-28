#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int cal(long long n) {
    if (n < 10) return 1 << n;
    return (1 << (n % 10)) | cal(n / 10);
}

int check(int n) {
    int state = 0;
    for (long long j = 1; ; j++) {
        state |= cal(j * n);
        if (state == 1023) return j;
    }
    
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", i);
        if (n == 0) printf("INSOMNIA\n");
        else printf("%lld\n", (long long)check(n) * n);
    }
    return 0;
}
