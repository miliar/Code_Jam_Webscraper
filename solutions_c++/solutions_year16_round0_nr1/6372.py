#include <bits/stdc++.h>
using namespace std;

void change(long long now, int &mask) {
    while (now) {
        int val = now % 10;
        now /= 10;
        mask |= (1 << val);
    }
}

int main() {
    int t, icase = 1;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", icase++);
        if (!n) {
            printf("INSOMNIA\n");
        }
        else {
            long long now = 0;
            int mask = 0;
            while (mask != 1023) {
                now += n;
                change(now, mask);
            }
            printf("%lld\n", now);
        }
    }
    return 0;
}
