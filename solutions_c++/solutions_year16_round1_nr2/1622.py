#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int T, cnt[2505], N, h;

    scanf("%d", &T);
    for(int x = 1; x <= T; ++x) {
        memset(cnt, 0, sizeof(cnt));
        scanf("%d", &N);
        for(int i = 0; i < (2*N-1)*N; ++i) {
            scanf("%d", &h);
            ++cnt[h];
        }

        printf("Case #%d:", x);
        for(int i = 0; i < 2505; ++i) {
            if(cnt[i] > 0 && cnt[i]%2 == 1) printf(" %d", i);
        }
        printf("\n");
    }


    return 0;
}
