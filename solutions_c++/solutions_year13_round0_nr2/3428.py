#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

const int MAXN = 1000;

int h_r[MAXN], h_c[MAXN];

void work() {
    int r, c;
    static int arr[MAXN][MAXN];
    scanf("%d %d\n", &r, &c);
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", arr[i] + j);
    for (int i = 0; i < r; i++)
    {
        int max = -1;
        for (int j = 0; j < c; j++)
            if (arr[i][j] > max) max = arr[i][j];
        for (int j = 0; j < c; j++)
            if (arr[i][j] != max) h_c[j] = arr[i][j];
        h_r[i] = max;
    }

    for (int j = 0; j < c; j++)
    {
        int max = -1;
        for (int i = 0; i < r; i++)
            if (arr[i][j] > max) max = arr[i][j];
        for (int i = 0; i < r; i++)
            if (arr[i][j] != max) h_r[i] = arr[i][j];
        h_c[j] = max;
    }

    //for (int i = 0; i < r; i++) printf("%d ", h_r[i]); puts("");
    //for (int j = 0; j < c; j++) printf("%d ", h_c[j]); puts("");

    bool flag = true;
    for (int i = 0; i < r && flag; i++)
        for (int j = 0; j < c && flag; j++)
            if (arr[i][j] != std::min(h_r[i], h_c[j]))
                flag = false;
    printf("%s\n", flag ? "YES" : "NO");
}

int main() {

    int T; 
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }

    return 0;
}
