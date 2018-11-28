#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int seen[10];

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        long long N;
        scanf("%lld", &N);
        long long res = 0;
        if(N != 0) {
            fill(seen, seen + 10, 0);
            for(int i = 1; ; ++i) {
                long long x = i * N;
                while(x != 0) {
                    int a = x % 10;
                    seen[a] = 1;
                    x /= 10;
                }
                bool done = true;
                for(int j = 0; j < 10; ++j) if(seen[j] == 0) done = false;
                if(done) {
                    res = i * N;
                    break;
                }
            }
            printf("Case #%d: %lld\n", test, res);
        } else {
            printf("Case #%d: INSOMNIA\n", test);
        }
    }

    return 0;
}
