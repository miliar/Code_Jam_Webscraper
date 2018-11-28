#include <algorithm>
#include <cstdio>
using namespace std;

const int MAXN = 10000;

int N, X;
int S[MAXN];
bool mark[MAXN];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        scanf("%d%d", &N, &X);

        for (int i = 0; i < N; ++i) scanf("%d", &S[i]);
        sort(S, S+N);
        fill(mark, mark+N, false);
        int answer = 0;

        for (int i = N-1; i >= 0; --i) {
            if (mark[i]) continue;
            ++answer;

            for (int j = i-1; j >= 0; --j)
                if (!mark[j] && S[i]+S[j] <= X) { mark[j] = true; break; }
        }

        printf("%d\n", answer);
    }

    return 0;
}
