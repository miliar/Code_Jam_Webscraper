#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, N, n, cnt, y;
    bool v[10];

    scanf("%d", &T);
    for(int x = 1; x <= T; ++x) {
        scanf("%d", &N);

        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", x);
            continue;
        }

        cnt = 0;
        memset(v, false, sizeof(v));
        for(int i = 1; ; ++i) {
            n = N*i;
            while(n != 0) {
                if(v[n%10] == false) {
                    v[n%10] = true;
                    ++cnt;
                }
                n /= 10;
            }

            if(cnt >= 10) {
                y = N*i;
                break;
            }
        }

        printf("Case #%d: %d\n", x, y);
    }


    return 0;
}
