#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int T, len, cnt;
    char S[105], c;

    scanf("%d", &T);
    for(int x = 1; x <= T; ++x) {
        scanf("%s", S);

        len = strlen(S);
        c = S[0];
        cnt = 0;
        for(int i = 1; i < len; ++i) {
            if(S[i] != c) {
                ++cnt;
                c = S[i];
            }
        }
        if(S[len-1] == '-') ++cnt;

        printf("Case #%d: %d\n", x, cnt);
    }


    return 0;
}
