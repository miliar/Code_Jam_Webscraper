#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    #ifdef LOCAL
//    freopen("in.txt", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif // LOCAL
    int T;
    T = 100;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        int n;
        scanf("%d", &n);
        if(!n) puts("INSOMNIA");
        else {
            int cnt = 0;
            long long a = n;
            for(int i = 1; i < 100000; i++) {
                long long b = a;
                while(b) {
                    int t = b % 10;
                    cnt |= 1 << t;
                    b /= 10;
                }
                if(cnt == 1023) {
                    printf("%lld\n", a);
                    break;
                }
                a += n;
            }
        }
    }
    return 0;
}
