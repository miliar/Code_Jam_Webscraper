#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

#define SIZE 10010

int T;
int N;
int X;
int S[SIZE];
int flag[SIZE];

int ans = 0;

bool cmp(const int &a, const int &b) {
    return a < b;
}

int
main()
{
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        scanf("%d %d", &N, &X);
        memset(S, 0, sizeof(S));
        for (int i = 0; i < N; ++i)
            scanf("%d", &S[i]);
        memset(flag, 0, sizeof(flag));
        ans = 0;
        sort(S, S+N, cmp);
        for (int i = N - 1; i >= 0; --i) {
            if (!flag[i]) {
                flag[i] = 1;
                ++ans;
                for (int j = i - 1; j >= 0; --j) {
                    if (S[j] + S[i] > X)
                        continue;
                    if (!flag[j]) {
                        flag[j] = 1;
                        break;
                    }
                }
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
