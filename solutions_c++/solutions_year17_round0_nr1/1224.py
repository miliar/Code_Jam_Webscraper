#include <bits/stdc++.h>
using namespace std;

const int MAXL = 1000;

int L, K;
char S[MAXL+1];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%s%d", S, &K);
        L = strlen(S);

        int answer = 0;
        for (int i = 0; i < L; ++i)
            if (S[i] == '-') {
                if (i+K > L) { answer = -1; break; }

                ++answer;
                for (int j = i; j < i+K; ++j)
                    S[j] = (S[j] == '-') ? '+' : '-';
            }

        if (answer == -1)
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        else
            printf("Case #%d: %d\n", t+1, answer);
    }

    return 0;
}
