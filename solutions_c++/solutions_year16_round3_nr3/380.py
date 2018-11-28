#include <bits\stdc++.h>
#define N 3
using namespace std;

struct Fit {
    int a, b, c;
};

int A, B, C, K;
bool ans[N][N][N];
int ansCount;
bool tmp[N][N][N];

int calculateCount(bool s[][N][N]) {
    int count = 0;
    for (int i = 0; i < A; i++)
        for (int j = 0; j < B; j++)
            for (int k = 0; k < C; k++)
                if (s[i][j][k])
                    count++;
    return count;
}

bool checkRep(Fit fit, int K) {
    int rep[3] = { 0 };
    for (int i = 0; i < C; i++) 
        if (tmp[fit.a][fit.b][i])
            rep[0]++;
    for (int i = 0; i < B; i++)
        if (tmp[fit.a][i][fit.c])
            rep[1]++;
    for (int i = 0; i < A; i++)
        if (tmp[i][fit.b][fit.c])
            rep[2]++;
    if (rep[0] >= K || rep[1] >= K || rep[2] >= K)
        return true;
    return false;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, c = 1;
    scanf("%d", &t);
    while (t--) {
        ansCount = 0;
        memset(ans, false, sizeof(ans));
        srand(time(0));
        scanf("%d%d%d%d", &A, &B, &C, &K);
        for (int time = 0; time <= 1000; time++) {
            memset(tmp, false, sizeof(tmp));
            for (int q = 0; q < 1000; q++) {
                Fit fit;
                fit.a = rand() % A;
                fit.b = rand() % B;
                fit.c = rand() % C;

                if (tmp[fit.a][fit.b][fit.c])    continue;

                if (!checkRep(fit, K)) 
                    tmp[fit.a][fit.b][fit.c] = true;
            }
            int tmpCount = calculateCount(tmp);
            if (tmpCount > ansCount) {
                for (int i = 0; i < A; i++)
                    for (int j = 0; j < B; j++)
                        for (int k = 0; k < C; k++)
                            ans[i][j][k] = tmp[i][j][k];
                ansCount = tmpCount;
            }                
        }
        printf("Case #%d: %d\n", c++, ansCount);
        for (int i = 0; i < A; i++)
            for (int j = 0; j < B; j++)
                for (int k = 0; k < C; k++)
                    if (ans[i][j][k])
                        printf("%d %d %d\n", i + 1, j + 1, k + 1);
    }
    return 0;
}