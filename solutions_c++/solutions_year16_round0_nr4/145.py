#include <bits/stdc++.h>
using namespace std;
const int N = 100005;

int ca;


void work() {
    int K , C , S;
    cin >> K >> C >> S;
    if (S < (K + C - 1) / C) {
        puts("IMPOSSIBLE");
        return;
    }
    static long long p[105];
    p[0] = 1;
    for (int i = 1 ; i < C ; ++ i) {
        p[i] = p[i - 1] * K;
    }
    for (int i = 0 ; i < (K + C - 1) / C ; ++ i) {
        long long x = 0;
        for (int j = i * C ; j < (i + 1) * C && j < K; ++ j) {
            x += j * p[j % C];
        }
        printf("%lld " , x + 1);
    }
    puts("");
}

int main() {
    int T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
