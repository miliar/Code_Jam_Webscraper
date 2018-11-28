#include <cstdio>
#include <cstdlib>
#include <cstring>

const int MAX_STR = 1000;
char buff[MAX_STR];
char str[100][MAX_STR];
int c[MAX_STR][100];


int mycmp(const void *a, const void *b) {
    if (*(int*)a < *(int*)b) return -1;
    if (*(int*)a == *(int*)b) return 0;
    return 1;
}

int main() {
    int T;
    scanf("%d",&T);
    for (int t = 0; t < T; t++) {
        int N;
        bool flag = true;

        scanf("%d", &N);

        memset(str, 0, sizeof(char)*MAX_STR*100);
        memset(c, 0, sizeof(int)*MAX_STR*100);
        for (int n = 0; n < N; n++) {
            scanf("%s", buff);
            str[n][0] = buff[0];
            c[0][n] = 1;
            int p = 0;
            for (int i = 1; i < strlen(buff); i++) {
                if (buff[i] == buff[i-1]) {
                    c[p][n]++;
                }else {
                    p++;
                    str[n][p] = buff[i];
                    c[p][n] = 1;
                }
            }
            if (strcmp(str[n], str[0]) != 0) {
                flag = false;
                break;
            }
        }
        if (!flag) {
            printf("Case #%d: Fegla Won\n", t+1);
        }else {
            int res = 0;
            for (int i = 0; i < strlen(str[0]); i++) {
                qsort(c[i], N, sizeof(int), mycmp);
                int median = c[i][N/2];
                for (int j = 0; j < N; j++) res += abs(c[i][j] - median);
            }
            printf("Case #%d: %d\n", t+1, res);
        }
    }
    return 0;
}
