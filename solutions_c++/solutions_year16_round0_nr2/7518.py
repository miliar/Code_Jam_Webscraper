#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output-B-large.txt", "w", stdout);

    long long T, caseNo = 1, moves, i, length;
    char S[105];

    scanf("%lld", &T);

    while (T--) {
        moves = 0;

        scanf(" %s", S);

        length = strlen(S);

        for (i = 1; i < length; i++) {
            if (S[i] != S[i - 1]) moves++;
        }

        if (S[length - 1] == '-') moves++;

        printf("Case #%lld: %lld\n", caseNo++, moves);
    }

    return 0;
}
