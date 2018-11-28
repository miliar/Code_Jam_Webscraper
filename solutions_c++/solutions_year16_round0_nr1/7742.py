#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

bool v[20];

int main() {
    int T;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ",t);
        long long n;
        scanf("%lld",&n);
        if (n == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        memset(v,0,sizeof(v));
        for (long long a = n; ; a += n) {
            long long tmp = a;
            for (; tmp != 0; tmp /= 10)
                v[tmp % 10] = 1;
            bool flag = 1;
            for (int i = 0; i <= 9; i++)
                if (! v[i]) {
                    flag = 0;
                    break;
                }
            if (flag) {
                printf("%lld\n",a);
                break;
            }
        }
    }
    return 0;
}

