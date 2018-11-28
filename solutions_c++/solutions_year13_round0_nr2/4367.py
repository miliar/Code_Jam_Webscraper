#include <iostream>
#include <stdio.h>
using namespace std;
int s[110][110];

int main () {
    int T,N,M,i;
    scanf("%d", &T);
    for (i = 1; i <= T; ++i) {
        scanf("%d%d", &N, &M);
        int j, k;
        for (j = 0; j < N; ++j)
            for (k = 0; k < M; ++k)
                scanf("%d", &s[j][k]);
        int flag = 0;
        for (j = 0; j < N; ++j)
            for (k = 0; k < M; ++k)
            {
                int l;
                flag = 0;
                for (l = 0; l < M; ++l)
                    if (s[j][l] > s[j][k])
                        break;
                if (l == M) flag = 1;

                if (flag == 0) {
                    for (l = 0; l < N; ++l)
                        if (s[l][k] > s[j][k])
                            break;
                    if (l == N) flag = 1;
                }
                //cout << i << j << endl;
                if (flag == 0) goto Label;
            }
        Label:
        cout << "Case #"<<i<<": ";
        if (flag == 0) cout << "NO\n";
        else cout << "YES\n";
    }
    return 0;
}
